from django.urls import path
from .views import UserProfileView, UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
