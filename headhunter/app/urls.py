from django.urls import path
from .views.resume_views import TestHomeView, CreateSummaryView, DetailSummaryView

resume_url = [
    path('', TestHomeView.as_view(), name='home'),
    path('summary/create', CreateSummaryView.as_view(), name='create_summary'),
    path('summary/<int:pk>/', DetailSummaryView.as_view(), name='detail_summary')
]

urlpatterns = []

urlpatterns += resume_url
