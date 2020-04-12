"""
send_email.py
send an email
"""
import os

from flask_mail import Message, Mail
from flask import Flask

app = Flask(__name__)
secret_mail_data = os.path.join("app", "secret_mail_data.py")
print(os.getcwd())
if os.path.isfile(secret_mail_data):
	from app.secret_mail_data import SecretMailData
	secret_mail = SecretMailData()
	username, pwd = secret_mail.email_username, secret_mail.email_password
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

def send_email(recipient, name):
	"""
	send email
	"""
	msg = Message("Staying Connected with Capital Agile Services",
		sender=username, recipients=[recipient])
	msg.body = f"Hello {name},\n"+\
		"\tThank you for choosing to stay connected with Capital Agile Services."+\
		"You have successfully signed up for our mailing list!"
	mail.send(msg)
