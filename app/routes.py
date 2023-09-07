
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kaiden'}
    post = [{'author': {'username': 'Ryan'},'text': 'The new season of Brigerton is fun!'},
            {'author': {'username': 'Ginger'},'text': 'Really? What was your favorite part'}]
    return render_template('index.html', title = 'home', user=user, post = post )

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for server {}, remember me: {}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for("index.html"))
    return render_template('login.html',title='Login',form=form)