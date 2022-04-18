from django import forms
from app.models import Summary, Vacancy, Response, WorkExperience, Education


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
        
        
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = []


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = []

