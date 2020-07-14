from django.db import models

class StudentRegisterModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    contact_no = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
