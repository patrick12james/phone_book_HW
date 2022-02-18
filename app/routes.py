from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegisterForm, LoginForm, PhonebookForm
from app.models import User, Phonebook

@app.route ('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=["GET","POST"])
def register():
    form=RegisterForm()
    if form.validate_on_submit():

        username=form.username.data
        password=form.password.data

        user_exists = User.query.filter(User.username == username)

        if user_exists:
            flash(f"User with username {username} already exists", "danger")
            return redirect(url_for('register'))

        User(username=username, password=password)
        flash("Thank you for registering!", "primary")
        return redirect(url_for('index'))
    return render_template('register.html',form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.query.filter(User.username == username)


        if not user or not user.check_password(password):

            flash('That username and/or password is incorrect', 'danger')
            return redirect(url_for('login'))


        login_user(user)
        flash('You have succesfully logged in', 'success')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/phonebook', methods=['GET', 'POST'])
@login_required
def phonebook():
    form = PhonebookForm()

    if form.validate_on_submit():
        name = form.name.data
        phonenumber = form.phonenumber.data
        email = form.email.data
        address = form.address.data

        Phonebook(name=name, phonenumber=phonenumber, email=email, address=address)
        return redirect(url_for('index'))

    return render_template('phonebook.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You have logged out", "secondary")
    return redirect(url_for('index'))
