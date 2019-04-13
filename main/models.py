from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_edu_resources = models.CharField(max_length=30)
    def __str__(self):
        return self.name + " " + self.surname

class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Semester(models.Model):
    semester = models.DecimalField(primary_key=True, decimal_places=0, max_digits=2)

class PointList(models.Model):
    point = models.DecimalField(decimal_places=2, max_digits=5)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    semester = models.OneToOneField(Semester, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "subject", "semester")
