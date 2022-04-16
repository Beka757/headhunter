from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, UserDetailsView, UserPasswordUpdateView, UserUpdateView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserDetailsView.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/password-update/', UserPasswordUpdateView.as_view(), name='user_update_password'),
]
