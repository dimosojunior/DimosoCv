from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from MyApp.models import *
from MyApp.forms import *
#from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from itertools import chain
import random
from django.contrib.auth.models import User, auth


# Create your views here.

def home(request):

	blog = Blog.objects.all().order_by('?')
	portfolio = Portfolio.objects.all().order_by('?')
	
	context = {
		"blog":blog,
		"portfolio":portfolio,

		
	}

	return render(request, 'MyApp/home.html',context)




def contact_me(request):
	

	form = ContactMeForm()
	if request.method == "POST":
		form = ContactMeForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()


			#HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
			username = request.POST.get('FullName')
			#last_name = request.POST['last_name']
			email = request.POST.get('email')
			subject = "SHUKURU NICOLAUS DIMOSO"
			message = f"Ahsante  {username} kwa kuwasiliana na mimi kupitia email: {email}, kwa mawasiliano zaidi wasiliana na mimi kupitia namba ya simu 0628 431 507 au kwa njia ya email: juniordimoso8@gmail.com"
			from_email = settings.EMAIL_HOST_USER
			recipient_list = [email]
			send_mail(subject, message, from_email, recipient_list, fail_silently=True)
			#messages.success(request, "Email Sent Successful!!!")
			return HttpResponse("Email Sent Successful!!!")