from django.shortcuts import render

from .forms import ContactForm

def index(request):
	return render(request, "index.html", {
		'contact_form':ContactForm()
	})
	
