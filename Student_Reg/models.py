from django.db import models

# Create your models here.
class Student_Details(models.Model):
    Std_ID=models.CharField(max_length=260, primary_key=True)
    name = models.CharField( max_length=260)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=100)
    phone=models.PositiveSmallIntegerField()
    email=models.EmailField()
