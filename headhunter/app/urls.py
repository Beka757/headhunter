from django.urls import path
from .views import TestHomeView

urlpatterns = [
    path('', TestHomeView.as_view(), name='home')
]
