from flask import Flask
from flask import current_app
from flask import Blueprint
from flask import jsonify

from .site.routes import site
from .api.routes import api
from .database import setup_mongo

from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup blueprints
app.register_blueprint(site)
app.register_blueprint(api)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# Setup flask_pymongo 
setup_mongo(app)

if __name__ == "__main__":
    app.run(debug=True)