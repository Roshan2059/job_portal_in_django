from home.models import Job, JobApplication, Employer, JobSeeker
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # Get the user info from the form data
        fn = request.POST.get("first_name")
        ln = request.POST.get("lastname")
        un = request.POST.get("username")
        em = request.POST.get("email")
        # role = request.POST.get("role")
        pw1 = request.POST.get("password")
        pw2 = request.POST.get("confirm_password")

        if pw1 == pw2:
            if User.objects.filter(email=em).exists():
                messages.info(request, 'This Email Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=un).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=un, password=pw1, email=em, first_name=fn, last_name=ln)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match!")
            return redirect('signup')
    else:
        return render(request, "register.html")


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
        