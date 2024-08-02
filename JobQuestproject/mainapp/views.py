from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import *


def allsignin(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.user_type == 'employer':
               return redirect('emdashboard')
            else:
               return redirect('canprofile')
        else:
            return redirect('emsignin')
   return render (request,'allsignin.html')
   

def index(request):
   jobs = JobInfo.objects.all()
   search = request.GET.get('search', '')
   location = request.GET.get('location', '')

   jobs = JobInfo.objects.all()

   if search:
      jobs = jobs.filter(
            Q(job_title__icontains=search) |
            Q(industry__icontains=search) |
            Q(department__icontains=search) |
            Q(position__icontains=search) |
            Q(job_description__icontains=search) |
            Q(job_requirements__icontains=search)
      )

   if location:
      jobs = jobs.filter(location__icontains=location)  # Assuming you have a 'location' field in JobInfo

   

   jobDict = {
      
      'jobs':jobs
   }
   return render (request,'index.html',jobDict)
   

def main(request):
   return render (request,'employer/main.html')


   

def joblist(request):
   jobs = JobInfo.objects.all()
   job_filtered= []
   if request.user.is_authenticated:
      for job in jobs :
         already_applied = Applicant.objects.filter(applicant = request.user , job = job).exists()
         job_filtered.append((job,already_applied))
   
   else:
      for job in jobs:
         job_filtered.append((job,False))


   jobdict ={
      'job_filtered':job_filtered,
      'jobs':jobs,
   }
   return render (request,'job_listing.html',jobdict)
   

def check(request):
   
   return render (request,'structure.html')

def job_details(request,jobid):
   job = get_object_or_404(JobInfo , id = jobid)

   return render (request,'job_details.html' , {'job': job})


@login_required
def signout(request):
   logout(request)
   return redirect('index')
   

   


def job_search(request):
    search = request.GET.get('search')
    location = request.GET.get('location')  # Corrected 'locaton' to 'location'
    
    # Initialize queryset with all jobs
    jobs = JobInfo.objects.all()
    
    # Apply filters based on search and location
    if search:
        jobs = jobs.filter(
            Q(job_title__icontains=search) |
            Q(industry__icontains=search) |
            Q(created_by__username__icontains=search)
        )
    
    if location:
        jobs = jobs.filter(industry__icontains=location)
    
    # Modify job_filtered to include whether the current user has already applied
    job_filtered = []
    if request.user.is_authenticated:
        for job in jobs:
            already_applied = Applicant.objects.filter(applicant=request.user, job=job).exists()
            job_filtered.append((job, already_applied))
    else:
        # If the user is not authenticated, assume they haven't applied to any jobs
        for job in jobs:
            job_filtered.append((job, False))
    
    jobDict = {
        'job_filtered': job_filtered,
        'jobs': jobs
    }
    
    return render(request, 'job_search.html', jobDict)



@login_required
def changepassword(request):
   current_user = request.user
   if request.method == 'POST':
      currentPassword = request.POST.get('currentPassword')
      newPassword = request.POST.get('newPassword')
      confirmPassword = request.POST.get('confirmPassword')
      if newPassword == confirmPassword :
         if check_password(currentPassword , request.user.password):
            current_user.set_password(newPassword)
            current_user.save()
            
            update_session_auth_hash(request,current_user)
            if current_user.user_type == 'candidate':
               return redirect('canprofile')
            else:
               return redirect('emdashboard')
   return render(request , 'changepassword.html')


def blog_view(request):

   return render(request, 'blog.html')



 

# def searchpage(request):
#     search = request.GET.get('search', '')
#     location = request.GET.get('location', '')

#     jobs = JobInfo.objects.all()

#     if search:
#         jobs = jobs.filter(
#             Q(job_title__icontains=search) |
#             Q(industry__icontains=search) |
#             Q(department__icontains=search) |
#             Q(position__icontains=search) |
#             Q(job_description__icontains=search) |
#             Q(job_requirements__icontains=search)
#         )

#     if location:
#         jobs = jobs.filter(location__icontains=location)  # Assuming you have a 'location' field in JobInfo

#     job_filtered = [(job, Applicant.objects.filter(applicant=request.user, job=job)) for job in jobs]

#     jobDict = {
#         'job_filtered': job_filtered
#     }
#     return render(request, 'common/searchpage.html', jobDict)