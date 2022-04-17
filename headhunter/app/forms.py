from django import forms
from app.models import Summary, Vacancy, Response


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        exclude = ['user']


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ['user']
        
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        exclude = []

