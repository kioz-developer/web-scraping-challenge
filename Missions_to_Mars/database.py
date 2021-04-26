from flask_pymongo import PyMongo

mongo = PyMongo()

def setup_mongo(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_facts"
    mongo.init_app(app)
