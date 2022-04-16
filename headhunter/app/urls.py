from django.urls import path
from .views.resume_views import TestHomeView, CreateSummaryView, DetailSummaryView, ListSummaryView

from .views.vacancy_views import (
    VacancyCreateView, DetailVacancyView, ListVacancyView, VacancyCategoryView,
    SearchView
)

resume_url = [
    path('', TestHomeView.as_view(), name='home'),
    path('summary/create', CreateSummaryView.as_view(), name='create_summary'),
    path('summary/<int:pk>/', DetailSummaryView.as_view(), name='detail_summary'),
    path('summary/', ListSummaryView.as_view(), name='list_summary')
]

vacancy_url = [
    path('vacancy/create', VacancyCreateView.as_view(), name='create_vacancy'),
    path('vacancy/<int:pk>/', DetailVacancyView.as_view(), name='detail_vacancy'),
    path('vacancy/', ListVacancyView.as_view(), name='list_vacancy'),
    path('vacancy/<str:category>/', VacancyCategoryView.as_view(), name='vacancy_category'),
    path('search/', SearchView.as_view(), name='search')
]

urlpatterns = []

urlpatterns += resume_url
urlpatterns += vacancy_url
