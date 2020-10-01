from django.contrib import admin
from .models import Notes
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(Notes)

TokenAdmin.raw_id_fields = ["user"]
