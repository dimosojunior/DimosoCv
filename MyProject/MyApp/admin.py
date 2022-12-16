from django.contrib import admin
from . models import *

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ["Title", "Created", "Type"]
	search_fields = ["Title"]
	list_filter = ["Created"]

class BlogAdmin(admin.ModelAdmin):
	list_display = ["Title", "Created", "Type"]
	search_fields = ["Title"]
	list_filter = ["Created"]

class ContactMeAdmin(admin.ModelAdmin):
	list_display = ["FullName", "email", "phone","place","created"]
	search_fields = ["FullName","email"]
	list_filter = ["created"]

admin.site.register(Portfolio, PortfolioAdmin)	
admin.site.register(Blog, BlogAdmin)
admin.site.register(ContactMe, ContactMeAdmin)
