from flask import Flask
from datetime import datetime
from . import db
from flask_login import UserMixin

#Creating table that holds user information
class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    password = db.Column(db.String(20))
    
#Creating table that holds the blog information
class Blogpost(db.Model): 

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    content = db.Column(db.String(500))
    date_posted = db.Column(db.DateTime)