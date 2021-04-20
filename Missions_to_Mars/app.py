from flask import Flask,Blueprint
from .site.routes import site
from .api.routes import api

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api)

app.run(debug=True)