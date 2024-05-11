from flask import Flask#, render_template
import routes

app = Flask(__name__)

#from app import routes
#https://teamtreehouse.com/community/flask-import-issues

app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/index', 'index', routes.index)
app.add_url_rule('/dashboard', 'dashboard', routes.dashboard)

