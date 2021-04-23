from flask import Blueprint, render_template, request

site = Blueprint('site', __name__, template_folder='templates', static_folder='static')

@site.route('/')
def index():
    param = request.args.get("name")
    print(param)
    return render_template('index.html'), 200