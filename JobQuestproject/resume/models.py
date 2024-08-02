from django.db import models
from mainapp.models import*

# Create your models here.
class ResumeInp(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    # Skill
    skill1 = models.CharField(max_length=200, null=True)
    skill2 = models.CharField(max_length=200, null=True)
    skill3 = models.CharField(max_length=200, null=True)
    skill4 = models.CharField(max_length=200, null=True)
    skill5 = models.CharField(max_length=200, null=True)
    # EDUCATION 1
    degree1 = models.CharField(max_length=200, null=True)
    college1 = models.CharField(max_length=200, null=True)
    year1 = models.CharField(max_length=200, null=True)
    # EDUCATION 2
    degree2 = models.CharField(max_length=200, null=True)
    college2 = models.CharField(max_length=200, null=True)
    year2 = models.CharField(max_length=200, null=True)
    # EDUCATION 3
    degree3 = models.CharField(max_length=200, null=True)
    college3 = models.CharField(max_length=200, null=True)
    year3 = models.CharField(max_length=200, null=True)
    # LANGUAGAES
    lang1 = models.CharField(max_length=200, null=True)
    lang2 = models.CharField(max_length=200, null=True)
    lang3 = models.CharField(max_length=200, null=True)
    # PROJECT 1
    project1 = models.CharField(max_length=200, null=True)
    durat1 = models.CharField(max_length=200, null=True)
    desc1 = models.CharField(max_length=200, null=True)
    # PROJECT 2
    project2 = models.CharField(max_length=200, null=True)
    durat2 = models.CharField(max_length=200, null=True)
    desc2 = models.CharField(max_length=200, null=True)
    # EXPERICNECE 1 
    company1 = models.CharField(max_length=200, null=True)
    post1 = models.CharField(max_length=200, null=True)
    duration1 = models.CharField(max_length=200, null=True)
    lin11 = models.CharField(max_length=200, null=True)
    # EXPERICNECE 2
    company2 = models.CharField(max_length=200, null=True)
    post2 = models.CharField(max_length=200, null=True)
    duration2 = models.CharField(max_length=200, null=True)
    lin21 = models.CharField(max_length=200, null=True)
    # ACHIEVEMENT
    ach1 = models.CharField(max_length=200, null=True)
    ach2 = models.CharField(max_length=200, null=True)
    ach3 = models.CharField(max_length=200, null=True)



    def __str__(self):
        return self.name