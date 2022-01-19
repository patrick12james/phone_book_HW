from app import app
from flask import render_template
from app.forms import RegisterForm


@app.route('/home')
def home():
  home = 'Home'
  return render_template('home.html', home=home)

@app.route('/register', methods=["GET", "POST"])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    print('FORM HAS BEEN VALIDATED')
  return render_template('register.html', form=form)
