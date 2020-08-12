from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Notes)

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
