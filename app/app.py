from flask import Flask, render_template
# flask --app app/app.py run --x works

app = Flask(__name__)
print('app', app)

#from app import routes

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
    print('login form here')


def logout():
    # can be just a button
    pass

@app.route("/dashboard")
def dashboard():
    # data from eurostat
    # from test_api_eurostat notebook

    # format data flask pass json to javascript

    return render_template('dashboard.html', title='Dashboard')




"""
# This file contains the WSGI configuration required to serve up your
# web application at http://nurbujang.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://help.pythonanywhere.com/pages/DebuggingImportError


# +++++++++++ HELLO WORLD +++++++++++
# A little pure-wsgi hello world we've cooked up, just
# to prove everything works.  You should delete this
# code to get your own working.


HELLO_WORLD = <html></html>


def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = HELLO_WORLD
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')


# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.

# +++++++++++ VIRTUALENV +++++++++++
# If you want to use a virtualenv, set its path on the web app setup tab.
# Then come back here and import your application object as per the
# instructions below


# +++++++++++ CUSTOM WSGI +++++++++++
# If you have a WSGI file that you want to serve using PythonAnywhere, perhaps
# in your home directory under version control, then use something like this:
#
#import sys
#
#path = '/home/nurbujang/path/to/my/app
#if path not in sys.path:
#    sys.path.append(path)
#
#from my_wsgi_file import application  # noqa


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/nurbujang/mysite/mysite/settings.py'
## and your manage.py is is at '/home/nurbujang/mysite/manage.py'
#path = '/home/nurbujang/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()



# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
#import sys
#
## The "/home/nurbujang" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/nurbujang/myproject"
#path = '/home/nurbujang/mysite/to/flask_app_directory'
#if path not in sys.path:
#    sys.path.append(path)
#
#from main_flask_app_file import app as application  # noqa
#
# NB -- many Flask guides suggest you use a file called run.py; that's
## not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.
"""