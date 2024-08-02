from django.contrib import admin
from .models import *

class customUserDisplay(admin.ModelAdmin):
   list_display = ['username','user_type','email','mobile_number']

admin.site.register(CustomUser,customUserDisplay)
admin.site.register(Candidate)
admin.site.register(WorkExperience)
admin.site.register(AcademicQualification)
admin.site.register(JobInfo)
admin.site.register(CompanyProfile)
admin.site.register(ContactInformation)
admin.site.register(Skill)
admin.site.register(Applicant)
