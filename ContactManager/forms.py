import datetime

from django import forms

from .widgets import CustomDateWidget
from .models import Contact


class ContactForm(forms.ModelForm):

	AUTOFIELDS = {'first_name', 'last_name', 'address',
			'phone_number', 'email'}
			
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		# Add custom "v-model" attribute to each field rendered by the form
		for field_name, field_object in self.fields.items():
			if field_name in self.AUTOFIELDS:
				field_object.widget.attrs.update({
					'v-model':'contact.'+field_name
				})

	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'birthdate', 'address',
			'phone_number', 'email']
		widgets = {
			'birthdate': CustomDateWidget(
				attrs_month={'v-model':'form_birthdate.month'},
				attrs_day={'v-model':'form_birthdate.day'},
				attrs_year={'v-model':'form_birthdate.year'}
			),
			'phone_number': forms.TextInput(attrs={
				'placeholder':'e.g. 1800444555'
			})
		}