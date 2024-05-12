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
# https://help.pythonanywhere.com/pages/
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# https://jsonstat.com/explorer/#/https%3A%2F%2Fec.europa.eu%2Feurostat%2Fapi%2Fdissemination%2Fstatistics%2F1.0%2Fdata%2Favia_if_arp%3Flang%3DEN
# https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Getting+started+with+statistics+API
# https://ec.europa.eu/eurostat/databrowser/view/avia_if_arp/default/bar?lang=en&category=avia.avia_if
# https://ropengov.github.io/eurostat/reference/get_eurostat_json.html - R
# https://rdrr.io/cran/eurostat/man/get_eurostat_json.html - R
# https://www.youtube.com/watch?v=921Z4AgHwNY
# https://stackoverflow.com/questions/49590870/how-can-i-pass-json-of-flask-to-javascript
# https://www.reddit.com/r/flask/comments/tek82c/passing_a_json_object_from_flask_to_static_folde/?rdt=45690
# https://gist.github.com/ischurov/34fb9e3d2ccd7a177275adac98bde42b
# https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
# https://getbootstrap.com/docs/4.0/content/tables/
# https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Getting+started
# https://wikis.ec.europa.eu/display/EUROSTATHELP/API+Statistics+-+data+query
# https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Detailed+guidelines+-+API+Statistics
# https://stackoverflow.com/questions/50390889/pandas-data-mining-from-eurostat
# https://jsonstatpy.readthedocs.io/en/latest/notebooks/eurostat.html
# https://gist.github.com/ciaranjudge/43a9b3d9dacff77905e9eff59bc372c6 ###############
# https://www.kaggle.com/code/crischir/eurostat-api
# https://pypi.org/project/eurostat/
# https://pypi.org/project/jsonstat.py/
# immutablemultidict
# https://flask.palletsprojects.com/en/3.0.x/
# https://docs.sqlalchemy.org/en/20/core/engines.html
# https://plotly.com/javascript/plotlyjs-function-reference/
# https://stackoverflow.com/questions/25394493/truncate-table-only-if-it-exists-to-avoid-errors
# https://gcore.com/learning/how-to-delete-all-rows-mysql/
# 


