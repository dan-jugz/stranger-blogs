from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_required, login_user, logout_user
from ..models import Writer
from .forms import RegistrationForm, LoginForm
from .. import db
from ..writer import writer_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Stranger | Writer Login'
    login_form = LoginForm()
    if login_form.validate_on_submit():
        writer = Writer.query.filter_by(email=login_form.email.data).first()
        if writer is not None and writer.verify_password(login_form.password.data):
            login_user(writer, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('writer_user.dashboard'))
        flash('Invalid Writer_name or Password')
    return render_template('auth/login.html', title=title, login_form=login_form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    title =  'Alligator | Writer Sign Up'
    form = RegistrationForm()
    if form.validate_on_submit():
        new_writer = Writer(writer_name=form.writer_name.data, email=form.email.data, password=form.password.data)
        db.session.add(new_writer)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))