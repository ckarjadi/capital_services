"""
send_email.py
send an email
"""
import os

from flask_mail import Message, Mail
from flask import Flask

app = Flask(__name__)
secret_mail_data = os.path.join("app", "secret_mail_data.py")

if '_ON_HEROKU' not in os.environ:
	if os.path.isfile(secret_mail_data):
		from app.secret_mail_data import SecretMailData
		secret_mail = SecretMailData()
		username, pwd = secret_mail.email_username, secret_mail.email_password
	else:
		username, pwd = 'default_email_address@default.com', 'password'
else:
	from boto.s3.connection import S3Connection
	username, pwd = os.environ['EMAILADDRESS'], os.environ['EMAILPASSWORD']

app.config.update(dict(
	DEBUG = True,
	MAIL_SERVER = 'smtp.gmail.com',
	MAIL_PORT = 587,
	MAIL_USE_TLS = True,
	MAIL_USE_SSL = False,
	MAIL_USERNAME = username,
	MAIL_PASSWORD = pwd,
))

mail = Mail(app)
mail.init_app(app)

def send_email(subject, recipient, body):
	"""
	send email
	"""
	msg = Message(subject, sender=username, recipients=[recipient])
	msg.body = body
	mail.send(msg)
