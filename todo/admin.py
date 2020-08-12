from django.contrib import admin
from .models import *

admin.site.register(Todo)
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
