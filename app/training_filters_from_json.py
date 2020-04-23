"""
training_filters_from_json.py
get the training filters from the json file
"""
from app.reformat_json import load_json_file

def get_training_filters(json_file):
	"""
	get training filters from json file
	get default_values from json_file
	"""
	ct_filters, cb_filters, role_filters = [{} for _ in range(3)]
	data = load_json_file(json_file)
	ct_filters = {k: [v['course_type']] for k, v in data.items()}
	cb_filters = {k: [v['partner']] for k, v in data.items()}
	role_filters = {k: v['roles'] for k, v in data.items()}

	filter_to_obj = {"course_type_filter_list": ct_filters,
		"certifying_body_filter_list": cb_filters, "role_filter_list": role_filters}
	default_values = {'course_type_filter_list': 'ct_default',
		'certifying_body_filter_list': 'cb_default',
		'role_filter_list': 'role_default'}

	return {'filter_to_obj': filter_to_obj, 'default_values': default_values}
