function filterImages(divID, data)
	{
		let json_data = JSON.parse(data);
		let filter_to_obj = json_data['filter_to_obj'];
		let default_values = json_data['default_values'];
		let filters = document.getElementById("filters").getElementsByTagName("select");
		let images = document.getElementById(divID).getElementsByTagName("img");
		for (var j = 0; j < images.length; j++) {
			let booleans = [];
			let image = images[j];
			let image_id = image.id;
			let image_alt = image.alt; // index into ct, cb, role_filters
			for (var i = 0; i < filters.length; i++) {
				let filter = filters[i];
				let filter_object = filter_to_obj[filter.id]; // ct, cb, role_filters
				var accepted_values;
				if (image_alt in filter_object) {
					accepted_values = filter_object[image_alt]; // ['list_of_accepted_values']
				}
				let option_value = filter.value; // option value = "ct_default", "cb_default", etc.
				let decision = (default_values.includes(option_value) || accepted_values.includes(option_value))
				booleans.push(decision);
			}
			let li_id = image_id.replace('img', 'li');
			if (booleans.every(v=> v === true)) {
				
				document.getElementById(li_id).style.display = 'block';
				document.getElementById(image_id).style.display = 'block';
			} else {
				document.getElementById(li_id).style.display = 'none';
				document.getElementById(image_id).style.display = 'none';
			}
		}
	}

/*	ct_filters = {"cal1": ['cal1'], "leading_safe": ['leading_safe'],
		"safe_for_teams": ['safe_for_teams'], 'lean_portfolio_management': []}
	cb_filters = {"cal1": ['scrum_alliance'], "leading_safe": ['safe'],
		'safe_for_teams': ['safe'], 'lean_portfolio_management': []}
	role_filters = {}
	filter_to_obj = {"course_type_filter_list": ct_filters, "certifying_body_filter_list": cb_filters,
		"role_filter_list": role_filters}
	default_values = ['ct_default', 'cb_default', 'role_default']
	data = {'filter_to_obj': filter_to_obj, 'default_values': default_values}*/