from django.urls import path
from .views import*
urlpatterns = [
    path('',resume_inp,name='resume_inp'),
    path('resume/',resume,name='resume'),
]
