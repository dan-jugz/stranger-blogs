from flask import render_template, flash
from . import user
from ..request import get_random_quote
from ..writer import forms
from .. import db
from ..models import Blog, Subscriber
from ..email import mail_message

@user.route('/')
def home():
    title = 'Stranger Blogs'
    recent_blogs = Blog.get_posts()
    all_blogs = Blog.query.all()
    random_quote = get_random_quote()

    return render_template('index.html', title=title, all_blogs=all_blogs, recent_blogs=recent_blogs, random_quote=random_quote)

@user.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    title = "Stranger | Subscribe"
    form = forms.SubscribeForm()
    if form.validate_on_submit():
        if Subscriber.query.filter_by(email=form.email.data).first():
            flash('You are already subscribed')
        else:
            new_subscriber = Subscriber(email=form.email.data)
            db.session.add(new_subscriber)
            db.session.commit()
            subscribers = Subscriber.query.all()
            print("Subscribers are:", subscribers)
            for i in subscribers:
                mail_message("Thank you for subscribing", "email/thank_you", i.email)
            flash('Successfully subscribed!')
    
    return render_template('subscribe.html', form=form)
