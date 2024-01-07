from django.contrib import admin
from .models import Employer, Job, JobSeeker, JobApplication

all_models = [Employer, Job, JobApplication, JobSeeker]
admin.site.register(all_models)

