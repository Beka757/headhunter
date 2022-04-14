from django.urls import path
from .views.resume_views import TestHomeView, CreateSummaryView

resume_url = [
    path('', TestHomeView.as_view(), name='home'),
    path('summary/create', CreateSummaryView.as_view(), name='create_summary')
]

urlpatterns = []

urlpatterns += resume_url
