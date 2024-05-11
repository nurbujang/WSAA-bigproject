from flask import Flask#, render_template
import routes

app = Flask(__name__)

#from app import routes
#https://teamtreehouse.com/community/flask-import-issues

app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/index', 'index', routes.index)
app.add_url_rule('/dashboard', 'dashboard', routes.dashboard, methods=['GET', 'POST'])


# https://www.w3schools.com/jsref/met_win_alert.asp
# https://stackoverflow.com/questions/23205577/python-flask-immutablemultidict
# https://teamtreehouse.com/community/flask-import-issues
# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
# https://getbootstrap.com/docs/5.3/components/buttons/#button-tags
# https://blog.pythonanywhere.com/121/
# https://help.pythonanywhere.com/pages/UsingMySQL/
# https://python-web.teclado.com/section07/lectures/06_jinja2_conditional_statements/


