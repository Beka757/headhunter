from django import forms
from app.models import Summary


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        exclude = ['user']
