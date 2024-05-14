from flask import render_template, request

import pandas as pd
import eurostat

import pymysql
from sqlalchemy import create_engine

import plotly.express as px
import plotly
import json

df = pd.read_csv('~/db.csv')
user = df['user'][0]
host = df['host'][0]
password = df['password'][0]
db = df['db'][0]


def index():

    html = ""
    user = {"username": "User"}
    return render_template("index.html", title="Home", user=user)


def euro_update():
    # get eurostat data
    avia = eurostat.get_data_df("avia_if_arp")
    avia.drop(columns=["freq"], inplace=True, errors="ignore")
    avia.rename(columns={"geo\\TIME_PERIOD": "country"}, inplace=True)
    avia_stack = avia.set_index(["tra_infr", "country"]).stack().to_frame()
    avia_stack.reset_index(inplace=True)
    # .sort_values(['tra_infr', 'country', 'level_2'])
    avia_stack.rename(columns={"level_2": "year", 0: "value"}, inplace=True)

    # insert and replace sql table
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
    # connection = pymysql.connect(host=host, user=user,
    #                     password=password, db=db)

    # create cursor
    # cursor=connection.cursor()
    # Execute the to_sql for writing DF into SQL
    rows = avia_stack.to_sql("aviation", engine, if_exists="replace", index=False)
    engine.dispose() # important to avoid multiple connections
    return json.dumps(rows)


def table_delete():
    # sql delete table
    connection = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = connection.cursor()
    #rows = cursor.execute("DROP TABLE IF EXISTS aviation")
    try:
        rows = str(cursor.execute("TRUNCATE TABLE aviation"))
    except Exception as e:
        print('table delete exception:', e)
        rows = str(-1)
        return json.dumps(rows)
    else:
        connection.close()
        return json.dumps(rows)


def table_read():

    # engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
    # rows = pd.read_sql('SELECT * from aviation WHERE country="IE"', engine)
    # engine.dispose()
    rows = restapi_read(None)
    fig = px.line(rows, x="year", y="value", color="tra_infr")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def restapi_read(country):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

    if country is None:
        rows = pd.read_sql('SELECT * from aviation WHERE country="IE"', engine)
        engine.dispose()
        return rows
    else:
        rows = pd.read_sql(f'SELECT * from aviation WHERE country="{country}"', 
                           engine)
        
        # to provide a browser-friendly output
        rows = json.loads(rows.to_json())
        return rows


def dashboard():

    # format data flask pass json to javascript
    if request.method == "POST":
        # access the value as {button name} immutable dict
        # if there is a list, convert to dict with flat=False
        #print('request method', request.form.to_dict(flat=False))
        if request.form.get("update") == "UPDATE":
            # pymysql to update the data table
            # need to also alert the user that the operation completed successfully

            #print("clicked the update button")
            rows = json.loads(euro_update())

            return render_template(
                "dashboard.html",
                title="Dashboard",
                useralert="update",
            )
        elif request.form.get("delete") == "DELETE":
            rows = json.loads(table_delete())
            #print('rows:', rows)
            if rows != -1:
                print("clicked delete", rows)
                return render_template(
                    "dashboard.html", title="Dashboard", useralert="delete"
                )
            else:
                print('error in delete')
                return render_template(
                    "dashboard.html", title="Dashboard", useralert="delete_error"
                )

        elif request.form.get("plot") == "PLOT":
            rows = table_read()  # json format
            return render_template("dashboard.html", title="Dashboard", graphJSON=rows)

    else:
        print("GET")

    return render_template("dashboard.html", title="Dashboard")
