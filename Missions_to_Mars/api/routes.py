from flask import current_app
from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from .scrape_mars import scrape
from flask_pymongo import PyMongo
from ..database import mongo

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
@jwt_required()
def index():
    return 'Api is running', 200

@api.route('/scrape')
@jwt_required()
def call_scrape():
    mars_facts = mongo.db.mars_facts
    data = scrape()
    mars_facts.update({}, data, upsert=True)
    return jsonify({'msg':"Scraped successful"}), 200

# Route to authenticate users and return JWTs.
@api.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
