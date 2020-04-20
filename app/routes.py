"""
routes.py
routing logic;
"""
from flask import render_template, request, session
from app import app
from app.forms import LoginForm, RegistrationForm
from app.training_filters_from_json import get_training_filters
from app.upcoming_courses_filters_from_json import get_upcoming_courses_filters
from app.course_data_from_json import get_course_data_from_json
from app.send_email import send_email
import os
import json

def jsonify(text):
	"""
	jsonify filter
	"""
	return json.dumps(text)

app.add_template_filter(jsonify)

STATIC_PATH = os.path.join('app', 'static')
COURSES_JSON = os.path.join(STATIC_PATH, 'json', 'courses_2020041828.json')

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
	json_file = COURSES_JSON
	data = get_training_filters(json_file)
	kwargs = {'title': title, 'filter_data': data}
	return render_template(template_name, **kwargs)

@app.route('/upcoming_course')
def course_page():
	"""
	upcoming_course render;
	"""
	title = 'Upcoming Course Page'
	template_name = 'upcoming_course.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/upcoming_courses')
def upcoming_courses():
	"""
	upcoming_courses render;
	"""
	title = 'Upcoming Courses'
	template_name = 'upcoming_courses.html'
	json_file = COURSES_JSON
	data = get_upcoming_courses_filters(json_file)
	kwargs = {'title': title, 'filter_data': data}
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
	if form.validate_on_submit():
		course_name = session.get('course_name')
		data = get_course_data_from_json(COURSES_JSON, course_name)
		class_name = data['course_title']
		start, end = data['start_date'], data['end_date']
		location = data['location']
		effort, cost = data['effort'], data['cost']
		name = form.name.data
		email = form.email.data
		kwargs = {'name': name, 'email': email, 'class_name': class_name, 'start': start,
			'end': end, 'location': location, 'effort': effort, 'cost': cost}
		
		header = f"Registration for {class_name} ({location})"
		body = f"Dear {name},\n"+\
			f"Thank you for signing up for {class_name} ({location})."+\
			"We are looking forward to your participation!\n"+\
			f"It begins on {start} and ends on {end}. The effort is {effort} and "+\
			f"the cost is ${cost}."
		send_email(header, email, body)
		return render_template('successful_registration.html', **kwargs)
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
	header = 'Staying Connected with Capital Agile Services'
	body = f"Hello {data['name']},\n"+\
		"\tThank you for choosing to stay connected with Capital Agile Services. "+\
		"You have successfully signed up for our mailing list!"
	send_email(header, data['email'], body)
	title = 'Stay Connected'
	template_name = 'stay_connected.html'
	kwargs = {'name': data['name']}
	return render_template(template_name, **kwargs)

@app.route('/courses/<course_name>')
def render_course(course_name):
	"""
	render course pages
	"""
	data = get_course_data_from_json(COURSES_JSON, course_name)
	session['course_name'] = course_name
	title = data['course_title']
	template_name = 'all_courses.html'
	kwargs = {'title': title}
	kwargs.update(data)
	return render_template (template_name, **kwargs)
