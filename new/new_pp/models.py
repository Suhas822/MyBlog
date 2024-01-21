from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=29)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    tname=models.CharField(max_length=20)