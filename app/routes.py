from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test'}
    posts = [
        {
            'author': {'username': 'William'},
            'body': 'I WILL OBEY BIG MOTHER'
        },
        {
            'author': {'username': 'Barry'},
            'body': 'I LOVE BIG MOTHER'
        }
    ]
    return render_template('index.html', title='WELCOME TO THE SYSTEM', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='CONSCRIPTION', form=form)

@app.route('/no_title')
def no_title():
    user = {'username': 'Moose'}
    return render_template('index.html', user=user)