from django import forms
from .models import Answer


class ResultForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
