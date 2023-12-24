from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Job, Employer, JobSeeker
from django.contrib.auth import logout

def home(request):
    jobs = Job.objects.all()
    comp = Employer.objects.all()
    return render(request, 'home.html', context={'jobs' : jobs, 'companies' : comp})
    # Additional logic for displaying job listings, login/registration, etc.

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

def employer_detail(request, employer_id):
    employer = get_object_or_404(Employer, pk=employer_id)
    return render(request, 'employer_detail.html', {'employer': employer})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = request.POST.get('role')  # Fetch the selected role from the form
            user = form.save()
            
            if role == 'employer':
                Employer.objects.create(user=user, company_name=username)
                # Additional fields for employer
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user:
                    login(request, authenticated_user)
                    return redirect('employer_dashboard')  # Redirect to employer dashboard
            elif role == 'job_seeker':
                JobSeeker.objects.create(user=user, name=username)
                # Additional fields for job seeker
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user:
                    login(request, authenticated_user)
                    return redirect('job_seeker_dashboard')  # Redirect to job seeker dashboard
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any desired page after login
        else:
            # Handle invalid login credentials here (e.g., show error message)
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login.html')