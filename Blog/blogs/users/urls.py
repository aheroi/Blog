"""define URLS schemas for users"""

from django import views
from django.urls import path, include
from .import views

app_name = 'users'
urlpatterns = [
    # include authorization by default
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]