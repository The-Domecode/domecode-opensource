from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Query(models.Model):
    CATEGORY = [
        ('General Development', 'General Development'),
        ('Web Development', 'Web Development'),
        ('CS', 'Computer Science'),
        ('About DomeCode', 'About DomeCode')
    ]

    title = models.CharField(max_length=240)
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL)
    content = RichTextField(null=True, blank=True)
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="query_likes")
    category = models.CharField(max_length=30, choices=CATEGORY, default='GEN')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True, max_length=256)

    def __str__(self):
        return self.title

    def likes_as_flat_user_id_list(self):
        return self.likes.values_list('id', flat=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'slug': self.slug})


class Answer(models.Model):
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="answer_likes")
    slug = models.SlugField(null=True, unique=True, max_length=256)
    isaccepted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        uniqueid = get_random_string(length=8)
        self.slug = slugify(uniqueid)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'slug': self.query.slug})


class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=False, max_length=256)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'slug': self.answer.query.slug})

    def save(self, *args, **kwargs):
        uniqueid = get_random_string(length=8)
        self.slug = slugify(uniqueid)
        super().save(*args, **kwargs)
