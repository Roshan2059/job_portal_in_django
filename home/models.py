from django.db import models
# from django.contrib.auth.models import User
from job import settings

User = settings.AUTH_USER_MODEL
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_description = models.TextField()
    # Other fields like company website, industry, etc.

    def __str__(self):
        return self.company_name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    job_location = models.CharField(max_length=100)
    requirements = models.TextField()
    # Other fields like job type (full-time, part-time), salary, etc.

    def __str__(self):
        return self.title

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='jobseeker@gmail.com')
    contact_information = models.CharField(max_length=100)
    skills = models.TextField()
    # Other fields like education, experience, resume, etc.

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    # Other fields like status (pending, accepted, rejected), additional documents, etc.

    def __str__(self):
        return f"{self.job_seeker.name} - {self.job.title}"
