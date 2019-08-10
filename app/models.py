from flask import Flask
from . import db

#Creating table that holds user information
class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    password = db.Column(db.String(20))
    