"""
routes.py
routing logic;
"""
from flask import render_template, request
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	"""
	index render;
	"""
	css = ''
	if request.method == "GET" and 'css' in request.args:
		css = request.args['css']
	title, page_title = 'Home', ''
	template_name = 'body.html'
	kwargs = {'title': title, 'page_title': page_title,
		'css': css}
	return render_template(template_name, **kwargs)

@app.route('/assessment')
def assessment():
	"""
	assessment render;
	"""
	title, page_title = 'Assessment', 'Assessment'
	template_name = 'assessment.html'
	kwargs = {'title': title, 'page_title': page_title}
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

'''
@app.route('/courses')
def courses():
	"""
	individual course render;
	"""
	title = 'Individual Courses'
	template_name = 'courses.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)
'''

@app.route('/upcoming_course')
def course_page():
	"""
	upcoming_course render;
	"""
	title = 'Upcoming Course Page'
	template_name = 'upcoming_course.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/course_description')
def first_course():
	"""
	course_description render;
	"""

	title = 'Course Title'
	template_name = 'course1.html'
	kwargs = {'title': title}

	return render_template (template_name, **kwargs)


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
	title, page_title = 'Resources', ''
	template_name = 'resources.html'
	kwargs = {'title': title, 'page_title': page_title}
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
	template_name = 'about_us.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)

@app.route('/contact_us')
def contact_us():
	"""
	contact;
	"""
	title = 'Contact Us'
	template_name = 'contact_us.html'
	kwargs = {'user': user, 'title': title}
	return render_template(template_name, **kwargs)
