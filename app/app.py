from flask import Flask#, render_template
import routes

app = Flask(__name__)
#print('app', app)

#from app import routes

app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/index', 'index', routes.index)
app.add_url_rule('/dashboard', 'dashboard', routes.dashboard)

