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
    email = db.Column(db.String(64),unique=True,index=True)
    profile_image=db.Column(db.String(64),default='default_profile.png')
    password_hash = db.Column(db.String(255))   
    writer_blog = db.relationship('Blog', backref="writer", lazy='dynamic')

    comments_user=db.relationship('Comment',backref='commenter',lazy="dynamic")
    subscriber_id=db.relationship('Subscriber',backref='writer',lazy='dynamic')
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


class Blog(db.Model):
    """
    This class allows to create blogs table that will have the following columns:
        1. id
        2. title
        3. body
        4. posted_at
        5. writer_id
        5. posted_by
        6. writer_url
        7. comment_id
    """
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    writer_url = db.Column(db.String)
    posted_by = db.Column(db.String)
    comment_id = db.relationship('Comment', backref="comment_ids", lazy="dynamic")
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_posts(cls):
        '''
        Function that fetches all blog posts regardless of the writer
        '''

        posts=Blog.query.order_by(Blog.posted_at.desc()).all()
        return posts

    @classmethod
    def get_user_posts(cls,writer_id,page):
        '''
        Function that fetches all blog posts for a single writer
        '''
        posts_user=Blog.query.filter_by(author=writer_id).order_by(Blog.date.desc()).paginate(page=page,per_page=5) 
        return posts_user   

    def __repr__(self):
        return f'PostID:{self.id}--Date{self.date}--Title{self.title}'    


class Comment(db.Model):
    """
    This class helps us to be able to create a comments table that has:
        1. id column
        2. comment column
        3. commented_on column
        4. blog_id column
    """
    
    __tablename = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    comment = db.Column(db.String)
    commented_on = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def save_comment(self):
        '''
        Function that saves a new comment
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comments(cls,blog_id):
        '''
        Function that fetches a specific post comment
        '''
        
        comments=Comment.query.filter_by(blog_id=blog_id).all()
        return comments



class Quote:
    """
    This class helps to design Quotes data to have:
        1. quote
        2. author
    """
    def __init__(self, quote, author):
        """
        This method allows us to instantiate an instance.
        
        """
        self.quote = quote
        self.author = author

class Subscriber(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key=True)
    subscriber = db.Column(db.String(12))
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    email = db.Column(db.String)
    


