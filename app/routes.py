from app import app


@app.route('/home')
def index():
  return 'Hello World'

@app.route('/register')
def name():
  my_name = 'Patrick'
  return f"Hi {my_name}"
