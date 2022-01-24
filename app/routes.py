from ctypes import addressof
from app import app
from flask import redirect, render_template, url_for
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
    name = form.name.data
    phone_number = form.phone_number.data
    address = form.address.data
    register = form.register.data
    print(name, phone_number, address, register)
    return redirect(url_for('index'))


  return render_template('register.html', form=form)
