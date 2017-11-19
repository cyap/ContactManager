from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	birthdate = models.DateField()
	address = models.CharField(max_length=255, blank=True)
	phone_number = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)