from flask import Flask
from routes.main import *

app = Flask(__name__)
app.secret_key = "VerySecret12345"


app.add_url_rule("/", 'index', index, methods=['GET'])

app.run("0.0.0.0", port=8080, debug=True)
