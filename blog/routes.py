from flask import render_template
from blog import app
from blog.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/login/')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register/')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass

    return render_template('register.html', title='Sign Up', form=form)
