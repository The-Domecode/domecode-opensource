from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Todo(models.Model):
	title = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content= models.CharField(max_length=450,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('todo:detail', kwargs={'pk': self.pk})
