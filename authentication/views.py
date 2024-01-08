from django import forms
from home.models import Job, JobApplication, Employer, JobSeeker
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # Get the user info from the form data
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['email']
        role = request.POST['role']
        pw1 = request.POST['password']
        pw2 = request.POST['confirm_password']

def login(request):
    # Your login logic here
    if request.method == 'POST':
        # Process login form submission
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,"login.html")

    #     if user is not None:
    #         if user.role == 'employer':
    #                 login(request, user)
    #                 # Redirect to the employer dashboard
    #                 return redirect('home')
    #         elif user.role == 'job_seeker':
    #                 login(request, user)
    #                 # Redirect to the job_seeker_dashboard dashboard
    #                 return redirect('job_seeker_dashboard')
    #     else:
    #         messages.info(request,'invalid username or password')
    #         return redirect('login')
    # else:
    #     return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login.html')
        