from flask_wtf import FlaskForm
from wtforms import StringField, TelField, SubmitField
from wtforms.validators import DataRequired, EqualTo



class RegisterForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  phone_number = TelField('Phone Numbers', validators=[DataRequired()])
  address = StringField('Address', validators=[DataRequired()])
  register = SubmitField('Register', validators=[DataRequired()])
