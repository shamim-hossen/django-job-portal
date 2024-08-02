from django.contrib.auth.forms import UserChangeForm , UserCreationForm , PasswordChangeForm , AuthenticationForm
from django import forms
from .models import *



class JobInfoForm(forms.ModelForm):
    class Meta:
        model = JobInfo
        fields = [
            'job_title', 'industry', 'department', 'position', 'application_deadline',
            'experience', 'job_description', 'job_requirements',
            'academic_qualifications', 'preferred_qualification', 'job_type',
            'salary_type', 'salary', 'currency', 'specific_gender', 'job_skills', 'number_of_vacancies'
        ]
        widgets = {
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            'job_description': forms.Textarea(attrs={'rows': 4}),
            'job_requirements': forms.Textarea(attrs={'rows': 4}),
            'job_skills': forms.Textarea(attrs={'rows': 4}),
        }
        



class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'website', 'headline', 'founded_date', 'category', 'description']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'}),
            'headline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter headline'}),
            'founded_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
        }

class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['phone', 'email', 'full_address', 'video']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'full_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter full address', 'rows': 3}),
            'video': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter video URL'}),
        }
        labels = {
            'phone': 'Enter Contact Phone',
            'email': 'Enter Contact Email',
            
        }

class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        fields = ['platform', 'url']
        widgets = {
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter social network URL'}),
        }

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [ 'date_of_birth', 'job_type', 'salary_type', 'currency_type', 'current_salary', 'resume_file']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'salary_type': forms.Select(attrs={'class': 'form-control'}),
            'currency_type': forms.Select(attrs={'class': 'form-control'}),
            'current_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter current salary'}),
            'resume_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['organization_name', 'start_date', 'end_date', 'currently_working_here', 'job_description']
        widgets = {
            'organization_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter organization name'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'currently_working_here': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter job description', 'rows': 4}),
        }

class AcademicQualificationForm(forms.ModelForm):
    class Meta:
        model = AcademicQualification
        fields = ['institute_name', 'degree_name', 'grade', 'start_date', 'end_date', 'description']
        widgets = {
            'institute_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter institute name'}),
            'degree_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter degree name'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter grade'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['years_of_experience']
        widgets = {
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter years of experience'}),
        }