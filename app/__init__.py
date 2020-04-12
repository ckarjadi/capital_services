"""
__init__.py
init file;
"""
from flask import Flask
from flask_mail import Mail, Message
# from secret_mail_data import SecretMailData
app = Flask(__name__)
# app.config.from_object(SecretMailData)
# app.config.update(
# 	DEBUG=True,
# 	MAIL_SERVER='smtp.gmail.com',
# 	MAIL_PORT=465,
# 	MAIL_USE_SSL=True,
# 	MAIL_USERNAME = app.config['email_username'],
# 	MAIL_PASSWORD = app.config['email_password']
# 	)
# mail = Mail(app)
from app import routes
