$(document).ready(function(){
	$('.filter_clear').click(function(){ 
	    $('#event_filter').val('courses').trigger('change');
	    $('#course_type_filter_list').val('ct_default').trigger('change');
		$('#country_filter').val('all_countries').trigger('change');
		$('#city_filter').val('all_cities').trigger('change');
		$('#trainer_filter').val('all_trainers').trigger('change');
		$('#partner_filter').val('partner_default').trigger('change');
		$('#start_date_input').val('').trigger('change');
		$('#end_date_input').val('').trigger('change');
	});
});