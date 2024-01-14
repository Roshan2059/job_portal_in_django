from django import forms
from home.models import Job, JobApplication, Employer, JobSeeker
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login



from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     else:
#         # if forms.is_valid():
#         # Get the user info from the form data
#             fn = request.POST['firstname']
#             ln = request.POST['lastname']
#             un = request.POST['username']
#             em = request.POST['email']
#             role = request.POST['role']
#             pw = request.POST['password']
            
#             try:
#                 User.objects.create_user(first_name = fn, last_name = ln, username=un, email=em, role=role, password=pw )
#                 return redirect('login')
#             except:
#                 messages.error(request, "please fill the form properly")
#                 return redirect('signup')
        

# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')
#     else:
#         username=request.POST["username"]
#         password=request.POST["password"]
#         # Checking for employers and job seekers
        
# # def user_login(request):
# #     if request.method == 'POST':
# #         username = request.POST.get('username')
# #         password = request.POST.get('password')
# #         user = authenticate(username=username, password=password)
# #         if user:
# #             login(request, user)
# #             return redirect('home')  # Redirect to the home page or any desired page after login
# #         else:
# #             # Handle invalid login credentials here (e.g., show error message)
# #             return render(request, 'login.html', {'error': 'Invalid username or password'})
# #     return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        # Get the user info from the form data
        fn = request.POST.get("firstname")
        ln = request.POST.get("lastname")
        un = request.POST.get("username")
        em = request.POST.get("email")
        role = request.POST.get("role")
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
                user = User.objects.create_user(username=un, password=pw1, email=em, first_name=fn, last_name=ln, position=role)
                user.save()
                # print('User created')
                if user is not None:
                    if user.position == "EMP":
                        auth_login(request, user)
                        return redirect('emp-dash')
                    elif user.position == "jobseeker":
                        return redirect('home')
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
            if user.position == "JS":
                return redirect('home')
            elif user.position == "EMP":
                return redirect('empdash')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,"login.html")
    
def logout_view(request):
    logout(request)
    return redirect('login.html')