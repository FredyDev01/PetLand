from django.contrib import admin
from .models import Person, Pet

# Register your models here.
admin.site.register([Person, Pet])