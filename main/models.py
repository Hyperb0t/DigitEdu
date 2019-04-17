from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class AdditionalEduResource(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.name + " " + self.surname


class ResourceToStudent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    resource = models.ForeignKey(AdditionalEduResource, on_delete=models.SET_DEFAULT, default= "")

    def __str__(self):
        return str(self.student) + " " + str(self.resource)

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PointList(models.Model):
    point = models.DecimalField(decimal_places=2, max_digits=5)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField("semester")

    class Meta:
        unique_together = ("student", "subject")

    def __str__(self):
        return self.student.__str__() + " " + self.subject.name + " " + self.semester.__str__()


class SessionBeginDate(models.Model):
    date = models.DateTimeField("Session begin date")


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total = models.PositiveSmallIntegerField("total")
    passed = models.PositiveSmallIntegerField("passed")

    class Meta:
        unique_together = ("group", "subject")

    def __str__(self):
        return self.subject.name + " " + self.group.name
