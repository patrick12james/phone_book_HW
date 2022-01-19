from app import app
from flask import render_template

@app.route('/home')
def home():
  home_page_name = 'Home'
  return render_template('home.html', home=home_page_name)

@app.route('/register')
def register():
  register_page_name = 'Register'
  return render_template('register.html', register=register_page_name)
