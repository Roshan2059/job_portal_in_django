from django import forms
from home.models import Job, JobApplication, Employer, JobSeeker
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # if forms.is_valid():
        # Get the user info from the form data
            fn = request.POST['firstname']
            ln = request.POST['lastname']
            un = request.POST['username']
            em = request.POST['email']
            role = request.POST['role']
            pw = request.POST['password']
            
            try:
                User.objects.create_user(first_name = fn, last_name = ln, username=un, email=em, role=role, password=pw )
                return redirect('login')
            except:
                messages.error(request, "please fill the form properly")
                return redirect('signup')
        

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username=request.POST["username"]
        password=request.POST["password"]
        # Checking for employers and job seekers
        
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('home')  # Redirect to the home page or any desired page after login
#         else:
#             # Handle invalid login credentials here (e.g., show error message)
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login.html')
        