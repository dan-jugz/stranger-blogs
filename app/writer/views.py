from flask import render_template, redirect, url_for, flash, request
from . import writer_user as writer
from ..models import Writer, Blog, Comment, Subscriber
from ..models import db
from flask_login import login_required, current_user
from .forms import NewBlogForm, EditBlogForm, CommentForm
import markdown2
from ..requests import get_random_quote
from ..email import mail_message

@writer.route('/home/dashboard', methods=["GET", 'POST'])
@login_required
def dashboard():
    title = "Writer Dashboard"
    blogs = Blog.query.filter_by(posted_by=current_user.writer_name).all()
    return render_template('writer/dashboard/dashboard.html', title=title, blogs=blogs)
