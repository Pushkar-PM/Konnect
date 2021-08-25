from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    department=models.CharField(max_length=25)
    year_of_study=models.CharField(max_length=20)