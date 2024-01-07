from django.contrib import admin
from django.urls import path
from authentication import views
urlpatterns = [
    path('login/', views.login, name='login'), 
    path('signup/', views.signup, name='signup'), 
    # Assuming 'home' is the app name for the home page
]
