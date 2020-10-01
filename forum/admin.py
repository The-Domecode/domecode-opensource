from django.contrib import admin
from .models import Query, Answer, Comment

# Register your models here.
admin.site.register(Query)
admin.site.register(Answer)
admin.site.register(Comment)
