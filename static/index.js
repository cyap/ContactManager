window.onload = function() {

	// Attach date validator to each day in dropdown
	$('#id_birthdate_1 > option').attr('v-if', function(i) {
		return 'this.validDay(' + (i+1) + ')'
	})
	
	new Vue({
		el: '#contact-submission', 
		data: {
			contact: { 
				birthdate: {
				},
				last_name: 'Test',
				address: 'ad'
			},
		},
		methods: {
			validDay: function(day) {
				// Check if each day can exist in selected month
				if(day > new Date(2020, this.contact.birthdate.month, 0).getDate())
					return false;
				return true;
			}	
		},
		delimiters: ['[[', ']]']
	});
}