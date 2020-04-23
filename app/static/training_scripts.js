function filterImages(divID, data)
	{
		let json_data = JSON.parse(data);
		let filter_to_obj = json_data['filter_to_obj'];
		let default_values = json_data['default_values'];
		let filters = document.getElementById("filters").getElementsByTagName("select");
		let date_inputs = document.getElementById("filters").getElementsByTagName("input");
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
				let current_default_value = default_values[filter.id];
				// filter.id = "course_type_filter_list";
				let decision = (current_default_value == option_value || accepted_values.includes(option_value))
				booleans.push(decision);
			}
			let start_date_input = date_inputs[0];
			let end_date_input = date_inputs[1];

			let actual_start_date = filter_to_obj[start_date_input.id][image_alt];
			let actual_end_date = filter_to_obj[end_date_input.id][image_alt];
			// index filter_to_obj by 'start_date_input', 'end_date_input'

			let input_start_date = start_date_input.value;
			let input_end_date = end_date_input.value;
			// get user input

			let default_start_date = default_values[start_date_input.id];
			let default_end_date = default_values[end_date_input.id];
			// get default values;
			if (input_start_date == default_start_date) {
				var start_within = true;
			} else {
				var start_within = dates.inRange(input_start_date, actual_start_date, actual_end_date);
			}
			
			if (input_end_date == default_end_date) {
				var end_within = true;
			} else {
				var end_within = dates.inRange(input_end_date, actual_start_date, actual_end_date);
			}
			
/*			console.log(image_alt);
			console.log('actual start' + actual_start_date);
			console.log('actual end' + actual_end_date);
			console.log('input start' + input_start_date);
			console.log('input end' + input_end_date);
			console.log('def start' + default_start_date);
			console.log('def end ' + default_end_date);
			console.log('start within' + start_within);
			console.log('end within' + end_within);*/
			booleans.push(start_within && end_within);
			
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

var dates = {
    convert:function(d) {
        // Converts the date in d to a date-object. The input can be:
        //   a date object: returned without modification
        //  an array      : Interpreted as [year,month,day]. NOTE: month is 0-11.
        //   a number     : Interpreted as number of milliseconds
        //                  since 1 Jan 1970 (a timestamp) 
        //   a string     : Any format supported by the javascript engine, like
        //                  "YYYY/MM/DD", "MM/DD/YYYY", "Jan 31 2009" etc.
        //  an object     : Interpreted as an object with year, month and date
        //                  attributes.  **NOTE** month is 0-11.
        return (
            d.constructor === Date ? d :
            d.constructor === Array ? new Date(d[0],d[1],d[2]) :
            d.constructor === Number ? new Date(d) :
            d.constructor === String ? new Date(d) :
            typeof d === "object" ? new Date(d.year,d.month,d.date) :
            NaN
        );
    },
    compare:function(a,b) {
        // Compare two dates (could be of any type supported by the convert
        // function above) and returns:
        //  -1 : if a < b
        //   0 : if a = b
        //   1 : if a > b
        // NaN : if a or b is an illegal date
        // NOTE: The code inside isFinite does an assignment (=).
        return (
            isFinite(a=this.convert(a).valueOf()) &&
            isFinite(b=this.convert(b).valueOf()) ?
            (a>b)-(a<b) :
            NaN
        );
    },
    inRange:function(d,start,end) {
        // Checks if date in d is between dates in start and end.
        // Returns a boolean or NaN:
        //    true  : if d is between start and end (inclusive)
        //    false : if d is before start or after end
        //    NaN   : if one or more of the dates is illegal.
        // NOTE: The code inside isFinite does an assignment (=).
       return (
            isFinite(d=this.convert(d).valueOf()) &&
            isFinite(start=this.convert(start).valueOf()) &&
            isFinite(end=this.convert(end).valueOf()) ?
            start <= d && d <= end :
            NaN
        );
    }
}