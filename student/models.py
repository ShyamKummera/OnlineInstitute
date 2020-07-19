from django.db import models

class StudentRegisterModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    contact_no = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

class StudentEnrolDetails(models.Model):
    enrol_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default=True)
    student_contact_no = models.IntegerField()
    course_name = models.CharField(max_length=60,default=True)