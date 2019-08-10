from flask import render_template, flash
from . import user


@user.route('/')
def home():
    title = 'Stranger Blogs'

    return render_template('index.html',title=title)