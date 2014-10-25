__author__ = 'Simon, Robert'

from server.database import db
from server.database.util.security import hash_password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(240), unique=False)
    is_online = db.Column(db.Boolean, unique=False)

    def __init__(self, username, email, password, is_online=False):
        self.username = username
        self.email = email
        self.password_hash = hash_password(password)
        self.is_online = is_online

    def __repr__(self):
        return '<User %r>' % self.username

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()