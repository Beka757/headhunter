from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    LogoutView, WorkExperienceCreateView, EducationCreateView, VacancyUpdateView,
    SummaryUpdateView
)

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('summary/experience/create/', WorkExperienceCreateView.as_view()),
    path('summary/education/create/', EducationCreateView.as_view()),
    path('vacancy/<int:pk>/update/', VacancyUpdateView.as_view()),
    path('summary/<int:pk>/update/', SummaryUpdateView.as_view())
]
