from flask import Blueprint

backend_app = Blueprint('backend_app', __name__)

@backend_app.route('/')
def backend_home():
    return 'Backend Home'

@backend_app.route('/users')
def backend_users():
    return 'Backend Users'

