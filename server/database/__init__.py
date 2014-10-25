__author__ = 'Simon'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Replace url for your instance!
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/app'
db = SQLAlchemy(app)
