from django.urls import path
from .views.resume_views import (
    CreateSummaryView, DetailSummaryView,
    ListSummaryView, SummaryCategoryView, SummarySearchView
)

from .views.vacancy_views import (
    VacancyCreateView, DetailVacancyView, ListVacancyView,
    VacancyCategoryView, VacancySearchView, UpdateVacancyView
)

resume_url = [
    path('summary/create', CreateSummaryView.as_view(), name='create_summary'),
    path('summary/<int:pk>/', DetailSummaryView.as_view(), name='detail_summary'),
    path('summary/', ListSummaryView.as_view(), name='list_summary'),
    path('summary/<str:category>/', SummaryCategoryView.as_view(), name='summary_category'),
    path('search/summary/', SummarySearchView.as_view(), name='summary_search')
]

vacancy_url = [
    path('vacancy/create', VacancyCreateView.as_view(), name='create_vacancy'),
    path('vacancy/<int:pk>/', DetailVacancyView.as_view(), name='detail_vacancy'),
    path('vacancy/', ListVacancyView.as_view(), name='list_vacancy'),
    path('vacancy/<str:category>/', VacancyCategoryView.as_view(), name='vacancy_category'),
    path('search/vacancy/', VacancySearchView.as_view(), name='vacancy_search'),
    path('vacancy/<int:pk>/update/', UpdateVacancyView.as_view(), name='update_vacancy')
]

urlpatterns = []

urlpatterns += resume_url
urlpatterns += vacancy_url
