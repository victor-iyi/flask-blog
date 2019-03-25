from flask import render_template
from blog import app


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/login/')
def login():
    return render_template('login.html', title='Sign In')


@app.route('/register/')
def register():
    return render_template('register.html', title='Sign Up')
