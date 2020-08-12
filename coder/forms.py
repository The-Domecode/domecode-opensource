from django import forms
from django.core.validators import FileExtensionValidator
from .models import Answer


class ResultForm(forms.ModelForm):
    result = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    
    class Meta:
        model = Answer
        fields = ['result']
