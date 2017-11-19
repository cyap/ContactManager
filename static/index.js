window.onload = function() {
	new Vue({
		el: '#contact-submission', 
		data: {
			contact: { 
				last_name: 'Test' 
			}
		},
		delimiters: ['[[', ']]']
	});
}