from django.contrib import admin
from loginapp.models import Migration
from loginapp.models import BmiData
# Register your models here.
# admin.py databases are registered here
admin.site.register(Migration)
admin.site.register(BmiData)
