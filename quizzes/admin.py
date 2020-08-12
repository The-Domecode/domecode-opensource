from django.contrib import admin
from .models import Ques, Answer, Quiz

admin.site.register(Quiz)
admin.site.register(Ques)
admin.site.register(Answer)
