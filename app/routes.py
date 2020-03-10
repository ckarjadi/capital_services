"""
routes.py
routing logic;
"""
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	"""
	index render;
	"""
	title = 'Home'
	user = {'username': 'Bob'}
	template_name = 'index.html'
	# posts = [
	# 	{
	# 		'author': {'username': 'John'},
	# 		'body': 'Some statement!'
	# 	},
	# 	{
	# 		'author': {'username': 'Sarah'},
	# 		'body': 'Another statement!'
	# 	}
	# ]
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/maturity_assessment')
def maturity_assessment():
	"""
	MA render;
	"""
	title = 'Maturity Assessment'
	user = {'username': 'Bob'}
	template_name = 'maturity_assessment.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/consulting')
def consulting():
	"""
	consulting render;
	"""
	title = 'Consulting'
	user = {'username': 'Bob'}
	template_name = 'consulting.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/coaching')
def coaching():
	"""
	coaching;
	"""
	title = 'Coaching'
	user = {'username': 'Bob'}
	template_name = 'coaching.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/training')
def training():
	"""
	training;
	"""
	title = 'Training'
	user = {'username': 'Bob'}
	template_name = 'training.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/courses')
def courses():
	"""
	courses;
	"""
	title = 'Courses'
	user = {'username': 'Bob'}
	template_name = 'courses.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/contact_us')
def contact_us():
	"""
	contact;
	"""
	title = 'Contact Us'
	user = {'username': 'Bob'}
	template_name = 'contact_us.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/about_us')
def about_us():
	"""
	about
	"""
	title = 'About Us'
	user = {'username': 'Bob'}
	template_name = 'about_us.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/login')
def login():
	"""
	login route
	"""
	title = 'Sign in'
	form = LoginForm()
	kwargs = {'title': title, 'form': form}
	return render_template('login.html', **kwargs)
