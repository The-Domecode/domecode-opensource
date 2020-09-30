from django.contrib import admin
from .models import Todo
from rest_framework.authtoken.admin import TokenAdmin

admin.site.register(Todo)

TokenAdmin.raw_id_fields = ["user"]
