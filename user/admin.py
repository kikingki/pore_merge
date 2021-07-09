from django.contrib import admin
from .models import Field, Career, CustomUser

# Register your models here.
admin.site.register(Field)
admin.site.register(Career)
admin.site.register(CustomUser)
