from django.urls import path,include
from mainapp.views import *
from .emviews import *
from .canviews import *


urlpatterns = [
   path('',index , name='index'),
   path('usersignin/',allsignin , name='allsignin'),
   path('check/',check , name='check'),
   path('main/',main , name='main'),
   # path('main/',main , name='main'),
   path('signout/',signout , name='signout'),
   path('job_details/<int:jobid>',job_details , name='job_details'),
   path('joblist/',joblist , name='joblist'),
   path('job_search/',job_search , name='job_search'),
   path('changepassword/',changepassword , name='changepassword'),
   
   
   path('employer-register/',emregister , name='emregister'),
   path('employer-emsignin/', emsignin, name='emsignin'),
   path('employer-emdashboard/', emdashboard, name='emdashboard'),
   path('employer-postedjob/', postedjob, name='postedjob'),
   path('employer-post-job/', job_post, name='job_post'),
   path('job/<int:jobid>/edit_job', edit_job, name='edit_job'),
   path('job/<int:jobid>/delete_job', delete_job, name='delete_job'),
   path('jobreject/<int:applicant_id>/', job_reject_view, name='jobreject'),
   path('jobcallinterview/<int:applicant_id>/', job_call_interview_view, name='jobcallinterview'),
   path('job/<int:jobid>/applicants/', applicants, name='applicants'),
   path('profile/emupdate/', emupdate_profile, name='emupdate_profile'),
   path('datefix/', datefix, name='datefix'),
   path('employer/profile/', view_employer_profile, name='view_employer_profile'),
   
   path('job/<int:jobid>/applyjob', applyjob, name='applyjob'),
   
   
   path('candidate-canregister/', canregister, name='canregister'),
   path('candidate-candidatesignin/', candidatesignin, name='candidatesignin'),
   path('candidate-canprofile/', canprofile, name='canprofile'),
   path('candidate-appliedjoblist/', appliedjoblist, name='appliedjoblist'),
   path('candidate/updatee/', update_candidate_profile, name='update_candidate_profile'),
   path('candidate/profile/', view_candidate_profile, name='view_candidate_profile'),
   path('blog_view/', blog_view, name='blog_view'),

   # Resume   
   path('resume/',include('resume.urls'))
   
]
