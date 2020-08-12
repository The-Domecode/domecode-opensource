# Generated by Django 3.0.8 on 2020-08-01 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_quiz_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ques',
            name='Language',
            field=models.CharField(choices=[('JAVA', 'Java'), ('PYTHON', 'Python'), ('RUST', 'Rust'), ('C++', 'C++'), ('General', 'General')], default='PYTHON', max_length=7),
        ),
    ]
