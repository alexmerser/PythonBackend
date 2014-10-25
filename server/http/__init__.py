__author__ = 'Simon, Robert'

from flask import Flask
from flask.ext import restful
from server.http.user import NewUser, User, Users

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(NewUser, '/users/', endpoint='newuser')
api.add_resource(User, '/users/<int:user_id>', endpoint='user')
api.add_resource(Users, '/users/', endpoint='users')