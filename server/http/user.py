__author__ = 'Simon ,Robert'

from flask import abort, g
from server.database import models
from flask.ext.restful import Resource, reqparse
from server.http.util.authentication import auth


class NewUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, location='json')
        self.parser.add_argument('email', type=str, required=True, location='json')
        self.parser.add_argument('password', type=str, required=True, location='json')
        super(NewUser, self).__init__()

    def post(self):
        args = self.parser.parse_args()
        user = User.query.filter_by(username=args['email']).first()
        if user is not None:
            return {'message': 'User exists'}, 401

        new_user = models.User(args['username'], args['email'], args['password'], True)

        new_user.create()
        return {'message': 'User created'}

class User(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, location='json')
        self.parser.add_argument('email', type=str, required=True, location='json')
        self.parser.add_argument('password', type=str, required=True, location='json')
        self.parser.add_argument('is_online', type=bool, required=False, default=True, location='json')
        super(User, self).__init__()

    def get(self, user_id):
        user = models.User.query.filter_by(id=user_id).first()
        if user is None:
            return {'message': 'User does not exist'}, 404
        return {'username': user.username, 'email': user.email, 'online': user.is_online}

    def put(self, user_id):
        args = self.parser.parse_args()
        if g.user.id != user_id:
            abort(404)
        updated_user = models.User(args['username'], args['email'], args['password'], args['is_online'])
        updated_user.update()
        return 200

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return {'message': 'User does not exist'}, 404

        user.delete()
        return {'username': user.username}

class Users(Resource):
    decorators = [auth.login_required]

    def get(self):
        user_list = models.User.query.all()
        return {'user list': self.jsonify_user_list(user_list)}

    def jsonify_user_list(self, list):
        jsonified_user_list = []

        for user in list:
            jsonified_user_list.append({'username': user.username, 'email': user.email, 'online': user.is_online})

        return jsonified_user_list
