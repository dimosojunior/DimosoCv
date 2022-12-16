from MyApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class ContactMeForm(forms.ModelForm):

	class Meta:
		model = ContactMe
		fields = '__all__'