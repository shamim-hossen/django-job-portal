from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
   email = models.EmailField(unique=True,null=True)
   mobile_number = models.PositiveIntegerField(null=True,unique=True)
   profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
   USER = [
      ('candidate','Candidate'),
      ('employer','Employer'),
      ('authority','Authority'),
   ]
   user_type = models.CharField(max_length=50, choices=USER, null=True)
   
   
   #Candidate


JOB_TYPE_CHOICES = [
    ('freelance', 'Freelance'),
    ('full_time', 'Full Time'),
    ('internship', 'Internship'),
    ('part_time', 'Part Time'),
    ('spot_time', 'Spot Time'),
]

GENDER_TYPE =[
    ('any','Any'),
    ('Male','Male'),
    ('Female','Female'),
]

SALARY_TYPE_CHOICES = [
    ('hourly', 'Hourly'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
    ('project_base', 'Project Base'),
]

CURRENCY_TYPE_CHOICES = [
    ('dollar', 'Dollar'),
    ('taka', 'Taka'),
]

ACADEMIC_QUALIFICATION_CHOICES = [
    ('PSC', 'Primary School Certificate (PSC)'),
    ('JSC', 'Junior School Certificate (JSC)'),
    ('SSC', 'Secondary School Certificate (SSC)'),
    ('HSC', 'Higher Secondary Certificate (HSC)'),
    ('Honours', 'Honours'),
    ('Masters', "Master's"),
    ('Phd', 'PhD'),
]

SOCIAL_PLATFORM_CHOICES = [
    ('facebook', 'Facebook'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),
    ('twitter', 'Twitter'),
]



class Candidate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10,null=True)
    date_of_birth = models.DateField(null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, null=True, blank=True)
    salary_type = models.CharField(max_length=20, choices=SALARY_TYPE_CHOICES, null=True, blank=True)
    currency_type = models.CharField(max_length=10, choices=CURRENCY_TYPE_CHOICES, null=True, blank=True)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    
    def __str__(self):
       return self.user.username + ' ' + self.job_type
      

class AcademicQualification(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=255,null=True)
    degree_name = models.CharField(max_length=100,null=True)
    grade = models.CharField(max_length=50,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)
    def __str__(self):
       return self.user.username + ' ' + self.institute_name

class WorkExperience(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE,null=True)
    organization_name = models.CharField(max_length=255,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working_here = models.BooleanField(default=False)
    job_description = models.TextField(null=True)
    def __str__(self):
       return self.user.username + ' ' + self.organization_name

class Skill(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE,null=True)
    years_of_experience = models.IntegerField(null=True)
    def __str__(self):
       return self.user.username + ' ' + self.years_of_experience

class CompanyProfile(models.Model):
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=255,null=True)
    website = models.URLField(null=True)
    headline = models.CharField(max_length=255,null=True)
    founded_date = models.DateField(null=True)
    category = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    def __str__(self):
       return self.employer.username + ' ' + self.company_name
    
    
class ContactInformation(models.Model):
    company_profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    full_address = models.TextField(null=True)
    video = models.URLField(null=True, blank=True)
    def __str__(self):
        if self.company_profile and self.phone:
            return self.company_profile.company_name + ' ' + self.phone
        return str(self.id)

class SocialNetwork(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=SOCIAL_PLATFORM_CHOICES,null=True)
    url = models.URLField(null=True)

class JobInfo(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    employer = models.ForeignKey(CompanyProfile,on_delete=models.DO_NOTHING, null=True)
    job_title = models.CharField(max_length=255,null=True)
    industry = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    application_deadline = models.DateField(null=True)
    specific_gender = models.CharField(choices= GENDER_TYPE , max_length=10, null=True, blank=True) 
    job_description = models.TextField(null=True)
    job_requirements = models.TextField(null=True)
    academic_qualifications = models.CharField(max_length=20, choices=ACADEMIC_QUALIFICATION_CHOICES,null=True)
    preferred_qualification = models.CharField(max_length=20, choices=ACADEMIC_QUALIFICATION_CHOICES, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES,null=True)
    salary_type = models.CharField(max_length=20, choices=SALARY_TYPE_CHOICES,null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_TYPE_CHOICES,null=True)
    experience = models.IntegerField(null=True)
    job_skills = models.TextField(null=True)
    number_of_vacancies = models.IntegerField(null=True)
    posted_date = models.DateField(auto_now_add=True,null=True,blank=True)
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)
    def __str__(self):
       return self.job_title + ' ' + self.job_type
   
    class Meta:
        ordering = ['-posted_date']


class Applicant(models.Model):
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    applicant=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='applicantinfo', null=True)
    skills=models.CharField(max_length=100,null=True)
    resume = models.FileField(upload_to='resumes/', null=True)
    cover_letter = models.TextField( null=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('reviewed', 'Reviewed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')] , default= 'pending')
    applied_at = models.DateTimeField(auto_now_add=True)
