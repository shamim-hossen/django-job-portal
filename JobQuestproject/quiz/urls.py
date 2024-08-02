from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:topic_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:topic_id>/result/', views.quiz_result, name='quiz_result'),
]
