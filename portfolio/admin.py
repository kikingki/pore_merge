from django.contrib import admin
from .models import Portfolio, Profile, Business

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Profile)
admin.site.register(Business)