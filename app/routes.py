from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return render_template('index.html', title='Home', user=user)

@app.route('/no_title')
def no_title():
    user = {'username': 'Moose'}
    return render_template('index.html', user=user)