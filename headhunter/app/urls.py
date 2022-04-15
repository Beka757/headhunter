from django.urls import path
from .views.resume_views import TestHomeView, CreateSummaryView

from .views.vacancy_views import VacancyCreateView

resume_url = [
    path('', TestHomeView.as_view(), name='home'),
    path('summary/create', CreateSummaryView.as_view(), name='create_summary')
]

vacancy_url = [
    path('vacancy/create', VacancyCreateView.as_view(), name='create_vacancy')
]

urlpatterns = []

urlpatterns += resume_url
urlpatterns += vacancy_url
