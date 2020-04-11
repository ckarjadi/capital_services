"""
reformat_json.py
module for reformatting the courses.json file
"""
from datetime import datetime
import os
import json

def date_ext(minutes=True, milliseconds=False):
	"""
	quick way to generate an extension based of the year/month/day;
	can include minutes if the boolean minutes flag is set to true.
	"""
	today = datetime.now()
	year_month_day = f"{today.year}{str(today.month).zfill(2)}{str(today.day).zfill(2)}"
	year_month_day_min = f"{year_month_day}{str(today.minute).zfill(2)}"
	if milliseconds:
		return f"{year_month_day_min}{str(today.microsecond)[:4]}"
	if not minutes:
		return year_month_day
	return year_month_day_min

def get_parent_path(filepath):
	"""
	exclude the last item in a filepath.
	M:\\scripts\\temp.txt -> temp.txt
	M:\\scripts - > M:
	M:\\scripts\\folder -> M:\\scripts
	"""
	path = os.sep.join(filepath.split(os.sep)[:-1])
	if path:
		return path
	return os.getcwd()

def load_json_file(filename):
	"""
	open a json-like file object
	"""
	with open(filename, 'r') as file:
		final = json.load(file)
	return final

def write_json(json_path, json_data, **kwargs):
	"""
	write json file
	"""
	sort_keys = kwargs.get('sort_keys', True)
	indent = kwargs.get('indent', 4)
	with open(json_path, 'w') as file:
		json.dump(json_data, file, sort_keys=sort_keys, indent=indent)
	print(json_path)

def reformat(json_file):
	"""
	reformat courses.json
	"""
	new_json = {}
	new_json_filename = os.path.join(f"{get_parent_path(json_file)}",
		f"courses_{date_ext()}.json")
	for json_object in load_json_file(json_file):
		new_json_object = {}
		for key, value in json_object.items():
			new_key = key.replace(' ', '_')
			if isinstance(value, dict):
				new_value = {}
				for inner_key, inner_value in value.items():
					new_value[inner_key.replace(' ', '_')] = inner_value
			else:
				if new_key == 'course_code':
					value = value.lower()
				new_value = value
			new_json_object[new_key] = new_value
		new_json[new_json_object['course_code']] = new_json_object
	write_json(new_json_filename, new_json)

def main():
	"""
	main entrypoint
	"""
	json_file = os.path.join('static', 'json', 'courses.json')
	print(json_file)
	print(os.path.isfile(json_file))
	reformat(json_file)

if __name__ == "__main__":
	main()
