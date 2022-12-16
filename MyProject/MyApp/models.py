from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

class Portfolio(models.Model):
	Title = models.CharField(max_length=1000)
	Image = models.ImageField(default="media/media/me.jpg", upload_to="media/", blank=True,null=True)
	Created = models.DateTimeField(auto_now_add=True)
	Type_Choices = (
			('web design','web design'),
			('web development','web development'),
			('computer vision','computer vision'),
			('automation','automation'),
		)
	Type = models.CharField(max_length=1000, choices=Type_Choices, blank=True, null=True)
	#UploadVideo = models.VideoField()

	def __str__(self):
		return self.Title


class Blog(models.Model):
	Title = models.CharField(max_length=1000)
	Link = models.CharField(max_length=1000, blank=True, null=True)
	Image = models.ImageField(default="media/media/me.jpg", upload_to="media/", blank=True,null=True)
	Created = models.DateTimeField(auto_now_add=True)
	Description = models.TextField(max_length=2000)
	Type_Choices = (
			('web design','web design'),
			('web development','web development'),
			('computer vision','computer vision'),
			('automation','automation'),
		)
	Type = models.CharField(max_length=1000, choices=Type_Choices, blank=True, null=True)
	#UploadVideo = models.VideoField()

	def __str__(self):
		return self.Title



class ContactMe(models.Model):
	FullName = models.CharField(max_length=1000)
	email = models.EmailField(max_length=1000)
	message = models.TextField(max_length=2000)
	phone = models.CharField(max_length=1000, default="+255")
	place = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.FullName
