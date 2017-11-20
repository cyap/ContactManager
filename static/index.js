/* 
	CSRF Token Configuration for POST requests. Code taken from
	https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
*/

/*******************/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*******************/

var testContact = {
	first_name: 'John',
	last_name: 'Doe',
	birthdate: '2/2/2017',
	address: '1200 Main Street',
	phone_number: 18004445555,
	email: 'johndoe@gmail.com'
}

var vueSubmit;
var vueList;

window.onload = function() {

	// Attach date validator to each day in dropdown
	$('#id_birthdate_1 > option').attr('v-if', function(i) {
		return 'this.validDay(' + (i+1) + ')'
	})
	
	vueSubmit = new Vue({
		el: '#contact-submission', 
		data: {
			contact: testContact,
			form_birthdate: {month:1, day:1, year:2017},
			errors: {'address':'test2'}
		},
		methods: {
			validDay: function(day) {
				// Check if each day can exist in selected month
				if(day > new Date(2020, this.form_birthdate.month, 0).getDate())
					return false;
				else
					return true;
			},
			add_contact: function(event) {
				event.preventDefault();
				event.stopPropagation();
				
				this.contact.birthdate = [
					this.form_birthdate.month,
					this.form_birthdate.day,
					this.form_birthdate.year
				].join('/');
				
				var scope = this;
				
				$.post('/add', JSON.stringify(this.contact), function(response) {
					console.log(response.errors);
					scope.errors.address = 'address';
					//scope.errors = response.errors;
					// Clear form
					// Errors
					// Refresh table view
				});
			}
			
		},
		delimiters: ['[[', ']]']
	});
	
	vueList = new Vue({
		el: '#contact-list',
		data: {
		
		},
		methods: {
			test: function() { console.log('test'); },
			delete_contact: function() {},
			update_contact: function() {},
		}
	})
}