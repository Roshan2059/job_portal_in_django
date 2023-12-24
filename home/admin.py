from django.contrib import admin
from .models import Employer, Job, JobSeeker, JobApplication

admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(JobSeeker)
admin.site.register(JobApplication)
