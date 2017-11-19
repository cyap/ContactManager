from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		# Add custom "v-model" attribute to each field rendered by the form
		for field_name, field_object in self.fields.items():
			field_object.widget.attrs.update({'v-model':'contact.'+field_name})

	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'birthdate', 'address',
			'phone_number', 'email']
		widgets = {
			#'birthdate': TODO: date widget
			'phone_number': forms.TextInput(attrs={
				'placeholder':'e.g. 1800444555'
			})
		}