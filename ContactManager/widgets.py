from django.forms import widgets


class CustomDateWidget(widgets.MultiWidget):
	""" Widget tailored for birthday selection, with dropdown for month/day and
		field for year. 
	"""
	
	DEFAULT_MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
		'Sep', 'Oct', 'Nov', 'Dec']
	DEFAULT_ATTRS = {'month':None, 'day':None, 'year':None}

	def __init__(self, attrs=None, attrs_month=None, attrs_day=None,
		attrs_year=None, month_labels=DEFAULT_MONTHS):
			months = [(val, lab) for lab, val in zip(month_labels, range(1,13))]
			days = [(day, day) for day in range (1, 32)]
		
			_widgets = (
				widgets.Select(attrs=attrs_month, choices=months),
				widgets.Select(attrs=attrs_day, choices=days),
				widgets.NumberInput(attrs=attrs_year),
			)
			super(CustomDateWidget, self).__init__(_widgets, attrs)
		
	def decompress(self, value):
		if value:
				return [value.day, value.month, value.year]
		return [None, None, None]
