"""
routes.py
routing logic;
"""
from flask import render_template, request, session
from app import app
from app.forms import LoginForm, RegistrationForm, StayConnectedForm, ContactUsForm
from app.training_filters_from_json import get_training_filters
from app.upcoming_courses_filters_from_json import get_upcoming_courses_filters
from app.course_data_from_json import get_course_data_from_json
from app.generate_mailto import gen_mailto
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

secret_mail_data_file = os.path.join("app", "secret_mail_data.py")

if '_ON_HEROKU' not in os.environ:
	if os.path.isfile(secret_mail_data_file):
		from app.secret_mail_data import SecretMailData
		CONTACT_US_EMAIL = SecretMailData().contact_us_email
	else:
		CONTACT_US_EMAIL = 'default_contact_us_email@default.com'
else:
	CONTACT_US_EMAIL = os.environ['CONTACT_US_EMAIL']

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	"""
	index render;
	"""
	css = ''
	if request.method == "GET" and 'css' in request.args:
		css = request.args['css']
	form = StayConnectedForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		header = 'Staying Connected with Capital Agile Services'
		body = f"Hello {name},\n"+\
			"\tThank you for choosing to stay connected with Capital Agile Services. "+\
			"You have successfully signed up for our mailing list!"
		send_email(header, email, body)
		kwargs = {'name': name, 'title': 'Stay Connected'}
		return render_template('stay_connected.html', **kwargs)
	title, page_title = 'Home', ''
	template_name = 'body.html'
	kwargs = {'title': title, 'page_title': page_title,
		'css': css, 'form': form}
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
	template_name = 'upcoming_course.html'
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
			f"Thank you for signing up for {class_name} ({location}). "+\
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

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
	"""
	contact;
	"""
	title = 'Contact Us'
	form = ContactUsForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		header = 'contact-us-ticket'
		body = f"{name} has contacted us.\nHere is their contact information:\n"+\
			f"\temail: {email}\n"+\
			f"\tphone: {form.phone.data}\n"+\
			f"\tcompany: {form.company.data}\n"+\
			f"Here are their comments:\n"+\
			f"{form.comments.data}"
		send_email(header, CONTACT_US_EMAIL, body)
		kwargs = {'name': name, 'title': title, 'email': email}
		return render_template('successful_contact_us.html', **kwargs)
	template_name = 'contact_us.html'
	kwargs = {'title': title, 'form': form}
	return render_template(template_name, **kwargs)

@app.route('/alt_contact_us')
def alt_contact_us():
	"""
	contact;
	"""
	title = 'Contact Us'
	template_name = 'alt_contact_us.html'
	kwargs = {'title': title}
	return render_template(template_name, **kwargs)

@app.route('/contact_us_email', methods=['POST'])
def contact_us_email():
	"""
	contact us email
	"""
	data = request.form
	name = data['name']
	subject = "Contacting Capital Agile Services"
	body = f"{data['comments']}"
	gen_mailto(subject, body)
	title = 'Contact Us'
	template_name = 'contact_us_email.html'
	kwargs = {'title': title, 'name': name}
	return render_template(template_name, **kwargs)

# @app.route('/stay_connected_email/', methods=['POST'])
# def stay_connected_email():
# 	"""
# 	send the stay connected email
# 	"""
# 	data = request.form
# 	header = 'Staying Connected with Capital Agile Services'
# 	body = f"Hello {data['name']},\n"+\
# 		"\tThank you for choosing to stay connected with Capital Agile Services. "+\
# 		"You have successfully signed up for our mailing list!"
# 	send_email(header, data['email'], body)
# 	title = 'Stay Connected'
# 	template_name = 'stay_connected.html'
# 	kwargs = {'name': data['name'], 'title': title}
# 	return render_template(template_name, **kwargs)

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
	return render_template	(template_name, **kwargs)
