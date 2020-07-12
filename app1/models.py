from django.db import models

class AdminLogin(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=20)

class ScheduleNewClass(models.Model):
    course_id = models.AutoField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=60)
    faculty = models.CharField(max_length=60)
    date_course_start = models.DateField()
    time_start = models.TimeField()
    fee = models.FloatField()
    duration = models.IntegerField(max_length=60)