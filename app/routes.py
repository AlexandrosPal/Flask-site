from flask import render_template, url_for, flash, redirect
from app.form import RegistrationForm
from app.models import Subscriber, Post
from app import app, db
import json

with open("app/posts.json", "r") as file:
    content = file.read()
    posts = json.loads(content)

@app.route("/")
@app.route("/Blog")
def blog():
    return render_template('blog.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        sub = Subscriber(name=form.name.data, email=form.email.data)
        print(sub)
        db.session.add(sub)
        db.session.commit()
        flash(f'Subscribed {form.name.data} to the newsletter!', 'success')
        return redirect(url_for('blog'))
    return render_template('register.html', form=form)