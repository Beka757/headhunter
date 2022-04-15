from django.urls import path
from .views.resume_views import TestHomeView, CreateSummaryView, DetailSummaryView

from .views.vacancy_views import VacancyCreateView, DetailVacancyView

resume_url = [
    path('', TestHomeView.as_view(), name='home'),
    path('summary/create', CreateSummaryView.as_view(), name='create_summary'),
    path('summary/<int:pk>/', DetailSummaryView.as_view(), name='detail_summary')
]

vacancy_url = [
    path('vacancy/create', VacancyCreateView.as_view(), name='create_vacancy'),
    path('vacancy/<int:pk>/', DetailVacancyView.as_view(), name='detail_vacancy')
]

urlpatterns = []

urlpatterns += resume_url
urlpatterns += vacancy_url
