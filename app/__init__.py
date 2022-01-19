from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'There is no key'

from . import routes
