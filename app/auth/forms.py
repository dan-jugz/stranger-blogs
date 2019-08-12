from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import Writer

class RegistrationForm(FlaskForm):
    writer_name = StringField('What writer-name would you like to use?', validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), EqualTo('confirm_password', message='Passwords ,must match')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self, data_field):
        if Writer.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is a writer with that email')
    def validate_writer_name(self, data_field):
        if Writer.query.filter_by(writer_name=data_field.data).first():
            raise ValidationError('That writer-name is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')