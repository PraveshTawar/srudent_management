from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=100,unique=True)
    
    

