from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Quiz(models.Model):
    CATEGORY = [
        ("EASY", "Easy Difficulty"),
        ("MEDIUM", "Medium Difficulty"),
        ("HARD", "Hard Difficulty"),
    ]
    Language = [
        ("java", "Java"),
        ("python", "Python"),
        ("rust", "Rust"),
        ("c++", "C++"),
        ("general", "General"),
    ]
    name = models.CharField(max_length=100)
    typeof = models.CharField(max_length=6, choices=CATEGORY, default="EASY", null=True)
    Language = models.CharField(max_length=10, choices=Language, default="python")
    slug = models.SlugField(null=True, unique=True, max_length=256)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Ques(models.Model):

    Choices = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")]
    Language = [
        ("JAVA", "Java"),
        ("PYTHON", "Python"),
        ("RUST", "Rust"),
        ("C++", "C++"),
        ("General", "General"),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    Language = models.CharField(
        max_length=7, choices=Language, default="PYTHON", null=True
    )
    solution = models.CharField(max_length=1, choices=Choices, default="A")
    slug = models.SlugField(null=True, unique=True, max_length=256)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Answer(models.Model):
    Choices = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")]
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL, related_name="quizuser"
    )
    question = models.ForeignKey(Ques, on_delete=models.CASCADE)
    iscorrect = models.BooleanField(default=False)
    answer = models.CharField(max_length=1, choices=Choices, default="A")
