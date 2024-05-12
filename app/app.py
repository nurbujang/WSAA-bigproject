from flask import Flask
import routes

app = Flask(__name__)

app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/index', 'index', routes.index)
app.add_url_rule('/dashboard', 'dashboard', routes.dashboard, methods=['GET', 'POST'])
app.add_url_rule('/aviation/<country>', 'aviation', routes.restapi_read, methods=['GET'])
app.add_url_rule('/delete', 'delete', routes.table_delete, methods=['GET'])