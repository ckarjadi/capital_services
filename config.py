"""
config.py
configuration file;
"""
import os

class Config():
	"""
	Configuration class;
	"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-key'
