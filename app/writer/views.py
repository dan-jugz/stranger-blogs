from flask import render_template, redirect, url_for, flash, request
from . import writer_user as writer
from ..models import Writer, Blog, Comment, Subscriber
from ..models import db
from flask_login import login_required, current_user
from .forms import NewBlogForm, EditBlogForm, CommentForm
import markdown2
from ..request import get_random_quote
from ..email import mail_message

@writer.route('/home/dashboard', methods=["GET", 'POST'])
@login_required
def dashboard():
    title = "Writer Dashboard"
    blogs = Blog.query.filter_by(posted_by=current_user.writer_name).all()
    return render_template('writer/blog/dashboard.html', title=title, blogs=blogs)


@writer.route('/writer/new_blog', methods=['POST', 'GET'])
@login_required
def new_blog():
    title = "New Blog"
    form = NewBlogForm()
    if form.validate_on_submit():
        form_title = form.title.data
        form_body = form.body.data
        form_writer_url = form.writer_url.data
        form_title = markdown2.markdown(form_title, extras=['code-friendly', 'fenced-code-blocks'])
        form_body = markdown2.markdown(form_body, extras=['code-friendly', 'fenced-code-blocks'])
        form_writer_url = markdown2.markdown(form_writer_url, extras=['code-friendly', 'fenced-code-blocks'])
        blog = Blog(title=form_title, body=form_body, posted_by=current_user.writer_name, writer_url=form_writer_url,)
        blog.save_blog()
        subscribers = Subscriber.query.all()
        print("Subscribers are:", subscribers)
        for i in subscribers:
            mail_message("New Post", "email/new_blog", i.email)
        flash("Blog successfully created. Check it out on your dashboard")
        return redirect(url_for('.new_blog'))
    return render_template('writer/blog/new_blog.html', title=title, form=form)

@writer.route('/writer/edit-article/<id>', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    title = 'Edit Blog'
    blog = Blog.query.filter_by(id=id).first()
    form = EditBlogForm()
    comment = Comment.query.filter_by(blog_id=blog.id).all()
    if form.validate_on_submit():
        if form.title.data:
            blog.title = form.title.data
            db.session.add(blog)
            db.session.commit()
        if form.body.data:
            blog.body = form.body.data
            db.session.add(blog)
            db.session.commit()
        if form.writer_url.data:
            blog.writer_url = form.writer_url.data
            db.session.add(blog)
            db.session.commit()
        return redirect(url_for('.edit_blog', id=blog.id))
    return render_template('writer/blog/edit_blog.html', blog=blog, form=form, title=title, id=id, comment=comment)

@writer.route('/blog', methods=['GET', 'POST'])
def home():
    title = "Stranger | Home"
    recent_blogs = Blog.query.order_by(Blog.posted_at.desc()).limit(6)
    all_blogs = Blog.query.all()
    random_quote = get_random_quote()
    return render_template('index.html', title=title, all_blogs=all_blogs, recent_blogs=recent_blogs, random_quote=random_quote)


@writer.route('/view/blog/<id>', methods=['GET', 'POST'])
def view_blog(id):
    ind_blog = Blog.query.filter_by(id=id).first()
    comment = Comment.query.filter_by(blog_id=ind_blog.id).all()
    title = 'Stranger'
    return render_template('writer/blog/ind_blog.html', title=title, ind_blog=ind_blog, id=id, comment=comment)

@writer.route('/comment/new/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    title = "Stranger | Comment Blog"
    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        title = markdown2.markdown(title, extras=["code-friendly", "fenced-code-blocks"])
        comment = markdown2.markdown(comment, extras=["code-friendly", "fenced-code-blocks"] )
        new_comment = Comment(title=title, comment=comment, blog_id=blog.id)
        new_comment.save_comment()
        return redirect(url_for('.view_blog', id=blog.id))
    return render_template('writer/comment/new_comment.html', form=form, blog=blog)


@writer.route('/delete/comment/<int:id>')
@login_required
def delete_comment(id):    
    comment = Comment.query.filter_by(id=id).first()
    ind_blog = Blog.query.filter_by(id=comment.blog_id).first()
    db.session.delete(comment)
    db.session.commit() 
    return redirect(url_for('.edit_blog', id=ind_blog.id))

@writer.route('/delete/blog/<int:id>')
@login_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('.dashboard'))


