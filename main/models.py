from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_edu_resources = models.CharField(max_length=30)

class Subject(models.Model):
    name = models.CharField(max_length=30)

class PointList(models.Model):
    points_list = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "subject")
