from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Question(models.Model):
    CATEGORY = [
        ('EASY', 'Easy Difficulty'),
        ('MEDIUM', 'Medium Difficulty'),
        ('HARD', 'Hard Difficulty'),
        ('ADVANCED', 'Advanced Difficulty'),
        ('IMPLEMENT', 'Implementation')
    ]
    TYPE = [
        ('JAVA', 'Java'),
        ('PYTHON', 'Python'),
        ('RUST', 'Rust'),
        ('C++', 'C++'),
        ('General', 'General')
    ]
    title = models.CharField(max_length=100)
    content = RichTextField()
    category = models.CharField(
        max_length=10, choices=CATEGORY, default='MEDIUM')
    typeof = models.CharField(max_length=10, choices=TYPE, default='PYTHON')
    solution = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to='media')
    slug = models.SlugField(null=True, unique=True, max_length =256)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('coder:detail', kwargs={'slug': self.slug})


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(
    ), null=True, on_delete=models.SET_NULL, related_name="submissionuser")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    iscorrect = models.BooleanField(default=False)
    result = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to='media', blank=True, null=True)
   # result = models.FileField( null= True, blank=True, default = 'media/media/output.txt',
    #   validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to= 'media')
