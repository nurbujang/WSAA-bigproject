#from app import app
from flask import render_template, request

#@app.route("/")
#@app.route("/index")
def index():
    # return 'Hello pilot!'

    html = ""

    # as PoC, display a chart
    # ref plotly: https://www.w3schools.com/graphics/tryit.asp?filename=tryplotly_bars
    # return 'Welcome, you can login now'

    user = {"username": "Folliitereito"}
    return render_template('index.html', title='Home', user=user)


def login():
    # need a form here
    pass


def logout():
    # can be just a button
    pass

#@app.route("/dashboard")
def dashboard():
    # data from eurostat
    # from test_api_eurostat notebook

    # format data flask pass json to javascript
    if request.method == 'POST':
        # access the value as {button name} immutable dict
        # if there is a list, convert to dict with flat=False
        if request.form.get('update') == 'update':
            # pymysql to update the data table
            # need to also alert the user that the operation completed successfully
            print('clicked the update button')
            return render_template('dashboard.html', title='Dashboard', useralert='update' )
        elif request.form.get('delete') == 'delete':
            # pymysql to delete the data table
            # alert user
            print('clicked delete')
            return render_template('dashboard.html', title='Dashboard', useralert='delete' )

        #print('request', request, request.form.to_dict(flat=True), request.form.get('update'))
    else:
        print('GET??')

    return render_template('dashboard.html', title='Dashboard')

# create table login (username varchar(250) NOT NULL, 
# password varchar(250) NOT NULL, 
# priviledge text);
# insert INTO login (username, password, priviledge) values ("admin", "password", "admin");
# select * from login;

# create table airport (country varchar(250) NOT NULL, 
# year (int), 
# main varchar(250),
# other varchar(250),
# small varchar(250)