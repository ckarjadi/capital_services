"""
forms.py;
login form;
"""
import phonenumbers
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
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
	name = StringField('Name', [DataRequired()], render_kw={"placeholder": "Name"})
	email = StringField('Email', [Email(message=('Not a valid email address.')),
		DataRequired()], render_kw={"placeholder": "Email"})
	# body = TextField('Message', [DataRequired(),
	# 	Length(min=4, message=('Your message is too short.'))])
	# recaptcha = RecaptchaField()
	submit = SubmitField('Sign Up')

class RegistrationForm(FlaskForm):
	"""
	registration form
	"""
	name = StringField('Name', [DataRequired()])
	email = StringField('Email', [Email(message=('Not a valid email address.')),
		DataRequired()])
	submit = SubmitField('Submit')

class ContactUsForm(FlaskForm):
	"""
	Contact Us Form
	"""
	name = StringField('Name', [DataRequired()], render_kw={'placeholder': 'Enter name'})
	email = StringField('Email', [Email(message=('Not a valid email address.')),
		DataRequired()], render_kw={'placeholder': 'Enter email address'})

	def validate_phone(form, field):
		"""
		validate phone number
		"""
		if len(field.data) > 16:
			raise ValidationError('Invalid phone number.')
		try:
			input_number = phonenumbers.parse(field.data)
			if not (phonenumbers.is_valid_number(input_number)):
				raise ValidationError('Invalid phone number.')
		except:
			input_number = phonenumbers.parse("+1" + field.data)
			if not (phonenumbers.is_valid_number(input_number)):
				raise ValidationError('Invalid phone number.')

	phone = StringField('Phone', validators=[DataRequired(), validate_phone],
		render_kw={'placeholder': 'Enter phone number'})
	company = StringField('Company', [DataRequired()], render_kw={'placeholder': 'Enter company name'})
	comments = TextAreaField('Comments/Questions', [DataRequired()],
		render_kw={'placeholder': 'Write something...'})
	submit = SubmitField('Submit')
