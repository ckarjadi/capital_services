"""
forms.py;
login form;
"""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
	"""
	login form;
	"""
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class StayConnectedForm(FlaskForm):
	"""
	Stay connnected form
	"""
	name = StringField('Name', [DataRequired()])
	email = StringField('Email', [Email(message=('Not a valid email address.')),
		DataRequired()])
	# body = TextField('Message', [DataRequired(),
	# 	Length(min=4, message=('Your message is too short.'))])
	recaptcha = RecaptchaField()
	submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
	"""
	registration form
	"""
	name = StringField('Name', [DataRequired()])
	email = StringField('Email', [Email(message=('Not a valid email address.')),
		DataRequired()])
	submit = SubmitField('Submit')
