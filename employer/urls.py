from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='empdash'), 
    path('emp-add-job/', views.add, name='emp-add-job'), 
    # Assuming 'home' is the app name for the home page
]