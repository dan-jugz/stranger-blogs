from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Writer.query.get(int(user_id))

class Writer(UserMixin,db.Model):
    """
    This class allows us to have a writers table that has the following columns:
        1. id
        2. writer_name
        3. email
        4. password
        5. writer_blog
    """
    __tablename__ = 'writers'
    id = db.Column(db.Integer, primary_key=True)
    writer_name = db.Column(db.String(50))
    email = db.Column(db.String)
    password_hash = db.Column(db.String(255))   
    writer_blog = db.relationship('Blog', backref="writer", lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('Access denied')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "Writer {}".format(self.writer_name)
