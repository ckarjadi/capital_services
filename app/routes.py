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
	template_name = 'body.html'
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

@app.route('/assessment')
def assessment():
	"""
	assessment render;
	"""
	title = 'Assessment'
	template_name = 'assessment.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/training')
def training():
	"""
	training render;
	"""
	title = 'Training'
	template_name = 'training.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/public_training')
def public_training():
	"""
	public_training render;
	"""
	title = 'Public Training'
	template_name = 'public_training.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/corporate_training')
def corporate_training():
	"""
	corporate_training render;
	"""
	title = 'Corporate Training'
	template_name = 'corporate_training.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/courses')
def courses():
	"""
	course_page render;
	"""
	title = 'Upcoming Courses'
	template_name = 'courses.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/course_page')
def course_page():
	"""
	course_page render;
	"""
	title = 'Course Page'
	template_name = 'course_page.html'
	kwargs = {'title': title}
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
	template_name = 'coaching.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/resources')
def resources():
	"""
	resources;
	"""
	title = 'Resources'
	template_name = 'resources.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/registration')
def registration():
	"""
	registration route
	"""
	title = 'Registration'
	form = LoginForm()
	kwargs = {'title': title, 'form': form}
	return render_template('registration.html', **kwargs)

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
