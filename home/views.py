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