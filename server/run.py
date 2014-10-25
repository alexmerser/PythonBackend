#!flask/bin/python
__author__ = 'Simon'

from server.http import app
from server.database import db

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)