from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class AdditionalEduResource(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_edu_resources = models.ForeignKey(AdditionalEduResource, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + self.surname



class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Semester(models.Model):
    semester = models.DecimalField(primary_key=True, decimal_places=0, max_digits=2)

    def __str__(self):
        return "Semester " + self.semester.__str__()

class PointList(models.Model):
    point = models.DecimalField(decimal_places=2, max_digits=5)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "subject", "semester")

    def __str__(self):
        return self.student.__str__() + " " + self.subject.name + " " + self.semester.__str__()

class SessionBeginDate(models.Model):
    date = models.DateTimeField

    def save(self, *args, **kwargs):
        self.pk = 1
        super(models.SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Lessons(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=3, decimal_places=0)
    passed = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        unique_together = ("group", "subject")

    def __str__(self):
        return self.subject.name + " " + self.group.name

