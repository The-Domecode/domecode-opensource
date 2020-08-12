from forum.models import Query
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Query)
admin.site.register(Answer)
admin.site.register(Comment)
