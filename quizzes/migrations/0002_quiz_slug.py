# Generated by Django 3.0.8 on 2020-08-01 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
