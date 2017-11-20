from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.core import serializers
from django.core.exceptions import ValidationError
#from django.utils.timezone import datetime

import json

from .forms import ContactForm
from .models import Contact

def index(request):
	return render(request, "index.html", {
		'contact_form':ContactForm()
	})
	
def list(request):
	return
	
def add(request):
	errors = {}
	contact = Contact(**json.loads(request.body))
	try:
		contact.full_clean()
		#contact.save()
	except ValidationError as e:
		errors = e.message_dict
	return JsonResponse(data={'errors':errors})
	
def delete(request):
	return
	
def update(request):
	return
	
