from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, UserDetailsView, LoginView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserDetailsView.as_view(), name='user_detail'),
]
