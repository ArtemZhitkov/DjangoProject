from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, email_verification, UserProfileDetailView, UserProfileUpdateView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/<int:pk>/', UserProfileUpdateView.as_view(), name='edit_profile'),
]
