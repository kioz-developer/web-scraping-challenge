from flask import Blueprint, render_template, request
from ..database import mongo

site = Blueprint('site', __name__, template_folder='templates', static_folder='static')

@site.route('/')
def index():
    data = mongo.db.mars_facts.find_one()
    return render_template("index.html", data=data), 200