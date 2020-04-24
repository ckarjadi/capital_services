"""
create_calendar_events_array.py
create calendar events array for fullcalendar.io calendar
"""
import os
import datetime
from reformat_json import load_json_file, date_ext, write_json, get_parent_path

def create_calendar_events_array(json_file):
	"""
	read each key, value pair
	get json data object
	"""
	events = []
	new_json_filename = os.path.join(f"{get_parent_path(json_file)}",
		f"event_array_{date_ext()}.json")
	for course_code, course_data in load_json_file(json_file).items():
		title = course_data['course_title']
		one_class = course_data['classes'][0]
		start = one_class['start date']
		end = one_class['end date']
		end_datetime = datetime.datetime.strptime(end, "%Y-%m-%d")
		end_datetime = end_datetime + datetime.timedelta(days=1)
		## want to pad by one date so that it displays properly on the calendar
		month = str(end_datetime.month).zfill(2)
		day = str(end_datetime.day).zfill(2)
		end = f"{end_datetime.year}-{month}-{day}"
		_id = course_code
		events.append({'title': title, 'start': start, 'end': end, 'id': _id,
			'url': f'courses/{course_code}'})
	write_json(new_json_filename, events)
	return new_json_filename

def main():
	"""
	main entrypoint
	"""
	json_file = os.path.join('static', 'json', 'courses_2020041828.json')
	create_calendar_events_array(json_file)

if __name__ == '__main__':
	main()
