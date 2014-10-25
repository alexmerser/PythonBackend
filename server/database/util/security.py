__author__ = 'Simon'

from passlib.apps import custom_app_context as pwd_context

def hash_password(password):
    return pwd_context.encrypt(password)

def verify_password_against_hash(password, password_hash):
    return pwd_context.verify(password, password_hash)

