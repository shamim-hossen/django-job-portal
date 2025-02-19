# Generated by Django 5.0.6 on 2024-06-26 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='name',
        ),
        migrations.AddField(
            model_name='applicant',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicantinfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='cover_letter',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.jobinfo'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes/'),
        ),
    ]
