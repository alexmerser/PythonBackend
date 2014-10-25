__author__ = 'Simon, Robert'

from flask import jsonify, make_response, g
from flask.ext.httpauth import HTTPBasicAuth
from server.database.models import User
from server.database.util.security import verify_password_against_hash

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email = email).first()
    if not user or not verify_password_against_hash(password, user.password_hash):
        return False
    g.user = user
    return True

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'message': 'Unauthorized access'}), 401)
