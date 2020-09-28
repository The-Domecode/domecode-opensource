from django.db import models
from django.db import models, transaction
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.crypto import get_random_string


class Resource(models.Model):

    LANGUAGE = [
        ("JAVA", "Java"),
        ("PYTHON", "Python"),
        ("RUST", "Rust"),
        ("C++", "C++"),
        ("General", "General"),
    ]
    title = models.CharField(max_length=100)
    serialno = models.IntegerField(null=True, blank=True)
    content = RichTextField()
    category = models.CharField(max_length=300)
    language = models.CharField(max_length=10,
                                choices=LANGUAGE,
                                default="PYTHON")
    slug = models.SlugField(null=True, unique=True, max_length=256)
    quizlink = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("resource:detail-python", kwargs={"slug": self.slug})


class Progress(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),
                             null=True,
                             on_delete=models.SET_NULL)
    isdone = models.BooleanField(default=False)
    slug = models.SlugField(null=True, unique=True, max_length=256)

    def save(self, *args, **kwargs):
        uniqueid = get_random_string(length=8)
        self.slug = slugify(uniqueid)
        super().save(*args, **kwargs)
