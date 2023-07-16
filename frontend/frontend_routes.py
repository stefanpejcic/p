from flask import Blueprint

frontend_app = Blueprint('frontend_app', __name__)

@frontend_app.route('/')
def frontend_home():
    return 'Frontend Home'

@frontend_app.route('/profile')
def frontend_profile():
    return 'Frontend Profile'

