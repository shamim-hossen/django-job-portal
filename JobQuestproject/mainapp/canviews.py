from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate , login , logout
from .models import *
from .forms import *
from django.contrib import messages



def canregister(request):
   if request.method == 'POST':
      fullName = request.POST.get('fullName')
      mobilenumber = request.POST.get('mobileNumber')
      email = request.POST.get('emailAddress')
      password = request.POST.get('password')
      
      user = CustomUser.objects.create_user(
         username=fullName,
         email=email,
         password=password,
         mobile_number=mobilenumber,
         user_type='candidate'  
      )
      user.save()
      # messages.success(request,'You successfully signup')
      return redirect('candidatesignin')
      
   return render(request, 'candidate/canregister.html')


def candidatesignin(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
         login(request, user)
         # messages.success(request,'You successfully Login')
         return redirect('canprofile')
      else:
         
         return redirect('candidatesignin')
      
   
   return render(request, 'candidate/candidatesignin.html')

@login_required
def canprofile(request):
   return render(request,'candidate/canprofile.html')


@login_required

def applyjob(request , jobid):
   job = get_object_or_404(JobInfo , id = jobid)
   
   already_applied = Applicant.objects.filter(applicant = request.user , job = job).exists()
   if already_applied:
      messages.warning(request,'You already applied ')
      return redirect('joblist')
   
   if request.method == 'POST':
      skills = request.POST.get('skills')
      resume = request.POST.get('resume')
      cover_letter = request.POST.get('cover_letter')
      
      applicant = Applicant.objects.create(
         skills = skills ,
         resume = resume,
         cover_letter = cover_letter ,
         job = job,
         applicant = request.user,
      )
      messages.success(request,'Applied Succesfully')

      return redirect('joblist')
      
   return render(request,'candidate/applyjob.html' , {'job': job , 'already_applied': already_applied})

# @login_required
# def appliedjoblist(request):
#    current_user = request.user
#    appliedjobs = Applicant.objects.filter(applicant = current_user)
   
   # already_applied = Applicant.objects.filter(applicant = current_user).exists()
   
   # jobdict = {
   #    'appliedjobs': appliedjobs,
   #    'already_applied':already_applied,
   # }
   
   # return render(request,'candidate/appliedjoblist.html',{'jobs'})


@login_required
def appliedjoblist(request):
    current_user = request.user
    appliedjobs = Applicant.objects.filter(applicant=current_user)
    
    jobdict = {
        'appliedjobs': appliedjobs,
    }

    return render(request, 'candidate/appliedjoblist.html', jobdict)
   
@login_required
def update_candidate_profile(request):
    user = request.user
    candidate = get_object_or_404(Candidate, user=user)
    
    WorkExperienceFormSet = inlineformset_factory(Candidate, WorkExperience, form=WorkExperienceForm, extra=1, can_delete=True)
    AcademicQualificationFormSet = inlineformset_factory(Candidate, AcademicQualification, form=AcademicQualificationForm, extra=1, can_delete=True)
    SkillFormSet = inlineformset_factory(Candidate, Skill, form=SkillForm, extra=1, can_delete=True)

    if request.method == 'POST':
        candidate_form = CandidateForm(request.POST,request.FILES, instance=candidate)
        work_experience_formset = WorkExperienceFormSet(request.POST, instance=candidate)
        academic_qualification_formset = AcademicQualificationFormSet(request.POST, instance=candidate)
        skill_formset = SkillFormSet(request.POST, instance=candidate)

        if candidate_form.is_valid() and work_experience_formset.is_valid() and academic_qualification_formset.is_valid() and skill_formset.is_valid():
            candidate_form.save()
            work_experience_formset.save()
            academic_qualification_formset.save()
            skill_formset.save()
            return redirect('profile')

    else:
        candidate_form = CandidateForm(instance=candidate)
        work_experience_formset = WorkExperienceFormSet(instance=candidate)
        academic_qualification_formset = AcademicQualificationFormSet(instance=candidate)
        skill_formset = SkillFormSet(instance=candidate)

    context = {
        'candidate_form': candidate_form,
        'work_experience_formset': work_experience_formset,
        'academic_qualification_formset': academic_qualification_formset,
        'skill_formset': skill_formset,
    }

    return render(request, 'profile/canupdate_profile.html', context) 
 
@login_required
def view_candidate_profile(request):
    user = request.user
   #  print(Candidate.user)
    candidate = Candidate.objects.get(user=user)
    work_experiences = WorkExperience.objects.filter(user=candidate)
    academic_qualifications = AcademicQualification.objects.filter(user=candidate)
    skills = Skill.objects.filter(user=candidate)
    
    context = {
        'candidate': candidate,
        'work_experiences': work_experiences,
        'academic_qualifications': academic_qualifications,
        'skills': skills,
    }
    
    return render(request, 'profile/view_candidate_profile.html', context)