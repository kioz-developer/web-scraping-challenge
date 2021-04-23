from flask import Flask
from flask import Blueprint
from flask import jsonify
from .site.routes import site
from .api.routes import api

from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup blueprints
app.register_blueprint(site)
app.register_blueprint(api)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True)