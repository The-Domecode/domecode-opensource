from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Question(models.Model):
    CATEGORY = [
        ("EASY", "Easy Difficulty"),
        ("MEDIUM", "Medium Difficulty"),
        ("HARD", "Hard Difficulty"),
        ("ADVANCED", "Advanced Difficulty"),
        ("IMPLEMENT", "Implementation"),
    ]
    TYPE = [
        ("JAVA", "Java"),
        ("PYTHON", "Python"),
        ("RUST", "Rust"),
        ("C++", "C++"),
        ("GO", "Go"),
        ("C", "C"),
        ("General", "General"),
    ]
    title = models.CharField(max_length=100)
    content = RichTextField()
    category = models.CharField(max_length=10,
                                choices=CATEGORY,
                                default="MEDIUM")
    typeof = models.CharField(max_length=10, choices=TYPE, default="PYTHON")
    solution = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=["txt"])],
        upload_to="media",
    )
    slug = models.SlugField(null=True, unique=True, max_length=256)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("coder:detail", kwargs={"slug": self.slug})


class Answer(models.Model):
    TYPE = [
        ("JAVA", "Java"),
        ("PYTHON", "Python"),
        ("RUST", "Rust"),
        ("C++", "C++"),
        ("GO", "Go"),
        ("C", "C"),
    ]

    user = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        related_name="submissionuser",
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    iscorrect = models.BooleanField(default=False)
    language = models.CharField(max_length=10, choices=TYPE,
                                default="PYTHON")  # Stores the language ofc

    status = models.CharField(max_length=100,
                              default="In Queue")  # Added the status field
    response_from_judge = models.TextField(null=True)
    # Stores the response received from judge. Can be helpful in debugging later.

    result = models.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=[
                "txt", "py", "java", "cpp", "c++", "rs", "go", "c"
            ])
        ],
        upload_to="media",
        blank=True,
        null=True,
    )  # Allowed for other types of file extensions


#    result = models.FileField( null= True, blank=True, default = 'media/media/output.txt',
#   validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to= 'media')
