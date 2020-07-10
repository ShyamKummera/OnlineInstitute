from django.db import models

class AdminLogin(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
