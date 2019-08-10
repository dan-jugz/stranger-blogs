from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class NewBlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()], render_kw={"placeholder": "Short but precise"})
    writer_url = StringField('Link to your website(optional)', render_kw={"placeholder": "To easily navigate readers to your website"})
    body = TextAreaField('Blog Body', render_kw={"placeholder": "Idealy should have atleast 300 characters"})
    submit = SubmitField('Create blog')


class EditBlogForm(FlaskForm):
    title = StringField('Change title')
    writer_url = StringField('Change link to your website')
    body = TextAreaField('New Body?')
    submit = SubmitField('Save changes')