#study mart
from django.db import models

# # Create your models here.
# class Organization(models.Model):
#     teacher_name = models.CharField(max_length=20)
#     course_name  = models.CharField(max_length=20)
#     course_duration = models.IntegerField(max_length=10)
#     seat = models.IntegerField()

#geekey
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
