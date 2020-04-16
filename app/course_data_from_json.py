"""
course_data_from_json.py
read course data from json in order to populate the page
"""
import os
import re
import datetime
from app.reformat_json import load_json_file


def get_start_end_date(one_class, length):
	"""
	get start and end date from one_class data object
	"""
	start_date = one_class['start date']
	start_date_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
	end_date_datetime = start_date_datetime + datetime.timedelta(days=length)
	return start_date, end_date_datetime.strftime(r"%Y-%m-%d")

def get_course_data_from_json(json_file, course_name):
	"""
	read course data from json in order to populate the page
	"""
	data = load_json_file(json_file).get(course_name)
	one_class = data['classes'][0]
	details = data['details']
	length = int(re.sub(r'[^0-9]', '', details['length']))

	start_date, end_date = get_start_end_date(one_class, length)
	location = f"{one_class['city']}, {one_class['country']}"

	return {'icon_file': data['icon_file'], 'course_title': data['course_title'],
		'start_date': start_date, 'end_date': end_date, 'location': location,
		'about_this_course': details['about_this_course'],
		'what_youll_learn': details['what_youll_learn'],
		'length': length, 'effort': details['effort'], 'cost': details['cost']}
