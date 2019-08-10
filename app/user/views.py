from flask import render_template, flash,request ,redirect ,url_for
from . import user
from request import get_random_quote

@user.route('/')
def home():
    title = 'Stranger Blogs'
    random_quote = get_random_quote()

    return render_template('user/home/home.html', title=title, random_quote=random_quote)

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
