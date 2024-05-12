# from app import app
from flask import render_template, request

import pandas as pd
import eurostat

import pymysql
from sqlalchemy import create_engine

# pip install plotly
import plotly.express as px
import plotly
import json


# replace with pythonanywhere mysql conn

user = "nurbujang"
host = f"{user}.mysql.pythonanywhere-services.com"
password = "rootroot"
db = f"{user}$wsaaproj"


def index():
    # return 'Hello pilot!'

    html = ""

    # as PoC, display a chart
    # ref plotly: https://www.w3schools.com/graphics/tryit.asp?filename=tryplotly_bars
    # return 'Welcome, you can login now'

    user = {"username": "Folliitereito"}
    return render_template("index.html", title="Home", user=user)


def login():
    # need a form here
    pass


def logout():
    # can be just a button
    pass


def dashboard():
    # data from eurostat
    # from test_api_eurostat notebook

    # format data flask pass json to javascript
    if request.method == "POST":
        # access the value as {button name} immutable dict
        # if there is a list, convert to dict with flat=False
        if request.form.get("update") == "UPDATE":
            # pymysql to update the data table
            # need to also alert the user that the operation completed successfully

            # query_update = "UPDATE airport SET main = %s WHERE ID = %s "

            print("clicked the update button")
            rows = euro_update()
            json = {"button": "update", "rows": rows}
            # c json can be passed and parsed
            return render_template(
                "dashboard.html",
                title="Dashboard",
                # useralert=json
                useralert="update",
            )
        elif request.form.get("delete") == "DELETE":

            # # query_delete = "DELETE FROM airport WHERE country=%s;"

            rows = table_delete()
            print("clicked delete", rows)
            return render_template(
                "dashboard.html", title="Dashboard", useralert="delete"
            )
        elif request.form.get("plot") == "PLOT":
            rows = table_read()  # json format
            return render_template("dashboard.html", title="Dashboard", graphJSON=rows)

            # pass rows to dashboard.html as something
            # as json or as plotly figure json
            # cleanest: https://efi.mit.edu/spring23/ex06/plotly
            # clean with beautifulsoup: https://www.reddit.com/r/flask/comments/xm23bq/comment/ipo5k35/
            # messy-ish with react: https://stackoverflow.com/questions/72930513/how-to-plot-plotly-chart-on-react-from-json-response-from-flask-api

        # print('request', request, request.form.to_dict(flat=True), request.form.get('update'))
    else:
        print("GET")

    return render_template("dashboard.html", title="Dashboard")


def euro_update():
    """
    add comments here
    https://stackoverflow.com/questions/58232218/how-to-insert-a-pandas-dataframe-into-mysql-using-pymysql
    """

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
    return rows


def table_delete():
    # sql delete table
    connection = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = connection.cursor()
    rows = cursor.execute("DROP TABLE IF EXISTS aviation")
    connection.close()
    return rows


def table_read():
    # connection = pymysql.connect(host=host, user=user, password=password, db=db)
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM aviation WHERE country="IE";')
    # rows = cursor.fetchall()

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
    rows = pd.read_sql('SELECT * from aviation WHERE country="IE"', engine)
    engine.dispose()
    fig = px.line(rows, x="year", y="value", color="tra_infr")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
    # return rows.to_json()


# query_create = create table login (username varchar(250) NOT NULL,
# password varchar(250) NOT NULL,
# priviledge text);

# ("insert INTO login (username, password, priviledge) values ("admin", "password", "admin");
# query_insert = ("INSERT INTO person " + "(personID, personname, age, salary, city) " + "VALUES (%s, %s, %s, %s, %s)")

# select * from login;

# create table airport (country varchar(250) NOT NULL,
# year (int),
# main varchar(250),
# other varchar(250),
# small varchar(250)
