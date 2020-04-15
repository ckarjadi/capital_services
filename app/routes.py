"""
routes.py
routing logic;
"""
from flask import render_template, request
from app import app
from app.forms import LoginForm, RegistrationForm
from app.training_filters_from_json import get_training_filters
from app.send_email import send_email
import os
import json

def jsonify(text):
	"""
	jsonify filter
	"""
	return json.dumps(text)

app.add_template_filter(jsonify)

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
	title, page_title = 'Assessment', ''
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
	json_file = os.path.join('app', 'static', 'json', 'courses_2020041224.json')
	data = get_training_filters(json_file)
	kwargs = {'title': title, 'filter_data': data}
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

	title = 'Leading SAFe'
	template_name = 'course1.html'
	kwargs = {'title': title}


	return render_template (template_name, **kwargs)

@app.route('/course_psm')
def second_course():
	"""
	course_description render;
	"""

	title = 'SM - Professional Scrum Master'
	template_name = 'course2.html'
	kwargs = {'title': title}

	return render_template (template_name, **kwargs)

@app.route('/course_csm')
def third_course():
	"""
	course_description render;
	"""

	title = 'CSM - Certified ScrumMaster'
	template_name = 'course3.html'
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

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	"""
	registration route
	"""
	title = 'Registration'
	form = RegistrationForm()
	kwargs = {'title': title, 'form': form}
	return render_template('registration.html', **kwargs)

@app.route('/about_us')
def about_us():
	"""
	about
	"""
	title = 'About Us'
	template_name = 'about_us.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/contact_us')
def contact_us():
	"""
	contact;
	"""
	title = 'Contact Us'
	template_name = 'contact_us.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/stay_connected_email/', methods=['POST'])
def stay_connected_email():
	"""
	send the stay connected email
	"""
	data = request.form
	send_email(data['email'], data['name'])
	title = 'Stay Connected'
	template_name = 'stay_connected.html'
	kwargs = {'name': data['name']}
	return render_template(template_name, **kwargs)