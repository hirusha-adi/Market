from flask import Flask
from routes.main import *
from database import settings

app = Flask(__name__)
app.secret_key = "VerySecret12345"


app.add_url_rule("/", 'index_no_page', index_no_page, methods=['GET'])
app.add_url_rule("/<page>", 'index', index, methods=['GET'])

app.run(
    settings.Web.host,
    port=settings.Web.port,
    debug=settings.Web.debug
)
