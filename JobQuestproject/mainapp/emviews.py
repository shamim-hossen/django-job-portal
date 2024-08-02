from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from mainapp.models import *
from django.contrib import messages
from .forms import *
from django.forms import inlineformset_factory

def emregister(request):
    if request.method == 'POST':
        username = request.POST.get('companyName')
        companylogo = request.POST.get('companylogo')
        companyName = request.POST.get('companyName')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            mobile_number=mobilenumber,
            profile_picture = companylogo,
            user_type='employer'  
            )
        
        company = CompanyProfile.objects.create(
            employer=user,
            company_name=companyName,
        )
        
        # messages.success(request, 'You have successfully signed up.')
        return redirect('emsignin')
    
    return render(request, 'employer/emregister.html')

def emsignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('emdashboard')
        else:
            return redirect('emsignin')
    
    return render(request, 'employer/emsignin.html')

@login_required
def emdashboard(request):
    
    return render(request,'employer/profilesec.html')

# @login_required
# def job_post(request):
#     if request.method == 'POST':
#         form = JobInfoForm(request.POST, request.FILES)
#         if form.is_valid():
#             f = form.save(commit=False)
#             try:
#                 company_profile = CompanyProfile.objects.get(employer=request.user)
#                 f.employer = company_profile
#                 f.created_by = request.user
#                 f.save()
#                 return redirect('postedjob')
#             except CompanyProfile.DoesNotExist:
#                 form.add_error(None, 'You must have a company profile to post a job.')
#     else:
#         form = JobInfoForm()
#     return render(request, 'employer/job_post.html', {'form': form})

@login_required
def job_post(request):
    if request.method == 'POST':
        form = JobInfoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            try:
                company_profile = CompanyProfile.objects.get(employer=request.user)
                f.employer = company_profile
                f.created_by = request.user
                f.save()
                return redirect('postedjob')
            except CompanyProfile.DoesNotExist:
                form.add_error(None, 'You must have a company profile to post a job.')
        else:
            print(form.errors) 
    else:
        form = JobInfoForm()

    return render(request, 'employer/job_post.html', {'form': form})


@login_required
def postedjob(request):
    try:
        company_profile = CompanyProfile.objects.get(employer=request.user)
        jobs = JobInfo.objects.filter(employer=company_profile)
    except CompanyProfile.DoesNotExist:
        jobs = []

    return render(request, 'employer/postedjob.html', {'jobs': jobs})



@login_required
def applicants(request, jobid):
    job = get_object_or_404(JobInfo, id = jobid)
    applicants = Applicant.objects.filter(job = job)

    return render(request, 'employer/applicants.html',{'job':job,'applicants':applicants})
    
@login_required
def job_reject_view(request, applicant_id):
    applicant = get_object_or_404(Applicant,id = applicant_id)
    applicant.status = 'rejected'
    applicant.save()
    jobid_a = applicant.job.id
    return redirect('applicants', jobid_a)
    
    
    
@login_required
def job_call_interview_view(request, applicant_id):
    applicant = get_object_or_404(Applicant,id = applicant_id)
    applicant.status = 'accepted'
    applicant.save()
    jobid_p = applicant.job.id
    return redirect('datefix')

@login_required
def datefix(request):
    
    return render(request,'employer/datefix.html')
    

@login_required
def edit_job(request, jobid):
    job = get_object_or_404(JobInfo, id=jobid)
    if request.method == "POST":
        form = JobInfoForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('postedjob')  
    else:
        form = JobInfoForm(instance=job)
    return render(request, 'employer/edit_job.html', {'form': form})





@login_required
def delete_job(request, jobid):
    job = JobInfo.objects.get(id = jobid)
    job.delete()
    return redirect('postedjob')

#i have to see

@login_required
def job_applicants(request, job_id):
    job = get_object_or_404(JobInfo, id=job_id, user=request.user)
    applicants = Applicant.objects.filter(job=job)
    return render(request, 'applicants.html', {'job': job, 'applicants': applicants})


@login_required
def delete_jobs(request, job_id):
    job = get_object_or_404(JobInfo, id=job_id, user=request.user)
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully')
        return redirect('posted_jobs')  # Redirect to the list of posted jobs
    
    return render(request, 'delete_job.html', {'job': job})



@login_required
def jo_detail(request, job_id):
    job = get_object_or_404(JobInfo, id=job_id)
    user = request.user

 
    is_candidate = user.groups.filter(name='Candidate').exists()

    # Check if the user has already applied for the job
    has_applied = Applicant.objects.filter(job=job, email=user.email).exists() if is_candidate else False

    if request.method == 'POST' and is_candidate and not has_applied:
        # Handle the job application
        Applicant.objects.create(
            job=job,
            name=user.get_full_name(),
            email=user.email,
            resume=request.FILES.get('resume'),
            cover_letter=request.POST.get('cover_letter'),
            status='pending'
        )
        messages.success(request, 'You have successfully applied for this job.')
        return redirect('job_detail', job_id=job_id)

    return render(request, 'job_detail.html', {'job': job, 'is_candidate': is_candidate, 'has_applied': has_applied})


@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(JobInfo, id=job_id)
    user = request.user

    # Check if the user is a candidate
    is_candidate = user.groups.filter(name='Candidate').exists()

    if not is_candidate:
        messages.error(request, 'Only candidates can apply for jobs.')
        return redirect('job_list')

    # Check if the user has already applied for the job
    has_applied = Applicant.objects.filter(job=job, email=user.email).exists()

    if has_applied:
        messages.info(request, 'You have already applied for this job.')
        return redirect('job_list')

    if request.method == 'POST':
        # Handle the job application
        Applicant.objects.create(
            job=job,
            name=user.get_full_name(),
            email=user.email,
            resume=request.FILES.get('resume'),
            cover_letter=request.POST.get('cover_letter'),
            status='pending'
        )
        messages.success(request, 'You have successfully applied for this job.')
        return redirect('job_list')

    return render(request, 'apply_for_job.html', {'job': job})

@login_required
def emupdate_profile(request):
    employer = request.user
    company_profile = get_object_or_404(CompanyProfile, employer=employer)
    contact_information, created = ContactInformation.objects.get_or_create(company_profile=company_profile)
    SocialNetworkFormSet = inlineformset_factory(ContactInformation, SocialNetwork, form=SocialNetworkForm, extra=1, can_delete=True)

    if request.method == 'POST':
        company_profile_form = CompanyProfileForm(request.POST, instance=company_profile)
        contact_information_form = ContactInformationForm(request.POST, instance=contact_information)
        social_network_formset = SocialNetworkFormSet(request.POST, instance=contact_information)

        if company_profile_form.is_valid() and contact_information_form.is_valid() and social_network_formset.is_valid():
            company_profile_form.save()
            contact_information_form.save()
            social_network_formset.save()
            return redirect('emdashboard')  # Redirect to a profile page after saving

    else:
        company_profile_form = CompanyProfileForm(instance=company_profile)
        contact_information_form = ContactInformationForm(instance=contact_information)
        social_network_formset = SocialNetworkFormSet(instance=contact_information)

    context = {
        'company_profile_form': company_profile_form,
        'contact_information_form': contact_information_form,
        'social_network_formset': social_network_formset,
    }

    return render(request, 'profile/emupdate_profile.html', context)
    

@login_required
def view_employer_profile(request):
    user = request.user
    company_profile = get_object_or_404(CompanyProfile, employer=user)
    contact_information = get_object_or_404(ContactInformation, company_profile=company_profile)
    social_networks = SocialNetwork.objects.filter(contact_information=contact_information)
    
    context = {
        'company_profile': company_profile,
        'contact_information': contact_information,
        'social_networks': social_networks,
    }
    
    return render(request, 'profile/view_employer_profile.html', context)