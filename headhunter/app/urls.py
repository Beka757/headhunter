from django.urls import path
from .views.resume_views import CreateSummaryView, DetailSummaryView, ListSummaryView

from .views.vacancy_views import VacancyCreateView, DetailVacancyView

resume_url = [
    path('summary/create', CreateSummaryView.as_view(), name='create_summary'),
    path('summary/<int:pk>/', DetailSummaryView.as_view(), name='detail_summary'),
    path('summary/', ListSummaryView.as_view(), name='list_summary')
]

vacancy_url = [
    path('vacancy/create', VacancyCreateView.as_view(), name='create_vacancy'),
    path('vacancy/<int:pk>/', DetailVacancyView.as_view(), name='detail_vacancy')
]

urlpatterns = []

urlpatterns += resume_url
urlpatterns += vacancy_url
