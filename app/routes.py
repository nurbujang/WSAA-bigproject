from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
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

@app.route("/dashboard")
def dashboard():
    # pull data from 

    return render_template('dashboard.html', title='Dashboard')
