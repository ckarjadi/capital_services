"""
upcoming_courses_filters_from_json.py
get the training filters from the json file
"""
from app.reformat_json import load_json_file

def get_upcoming_courses_filters(json_file):
	"""
	get upcoming courses filters from json file
	get default_values from json_file
	"""
	ct_filters, cb_filters, role_filters = [{} for _ in range(3)]
	data = load_json_file(json_file)

	ct_filters = {}
	start_dates = {}
	end_dates = {}
	partner_filters = {}
	event_filters = {}
	country_filters = {}
	city_filters = {}
	trainer_filters = {}

	for course_id, course_data in data.items():
		ct_filters[course_id] = [course_data['course_type']]
		partner_filters[course_id] = [course_data['partner']]
		event_filters[course_id] = [[]]
		one_class = course_data['classes'][0]
		start_dates[course_id] = one_class['start date']
		end_dates[course_id] = one_class['end date']
		country_filters[course_id] = [one_class['country']]
		city_filters[course_id] = [one_class['city']]
		trainer_filters[course_id] = [course_data['classes'][0]['instructor']]

	filter_to_obj = {'course_type_filter_list': ct_filters,
		'partner_filter': partner_filters, 'event_filter': event_filters,
		'country_filter': country_filters, 'city_filter': city_filters,
		'trainer_filter': trainer_filters,
		'start_date_input': start_dates,
		'end_date_input': end_dates}
	default_values = {'course_type_filter_list': 'ct_default',
		'partner_filter': 'partner_default', 'event_filter': 'courses',
		'country_filter': 'all_countries', 'city_filter': 'all_cities',
		'trainer_filter': 'all_trainers',
		'start_date_input': '',
		'end_date_input': ''}
	return {'filter_to_obj': filter_to_obj, 'default_values': default_values}
