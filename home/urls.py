from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define your home view URL here
    path('signup/', views.signup, name='signup'),  # URL for the signup page
    path('login/', views.user_login, name='login'),  # URL for the login page
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('employer/<int:employer_id>/', views.employer_detail, name='employer_detail'),
    # Add more paths for other functionalities or pages if needed
]
