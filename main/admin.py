from django.contrib import admin
from .models import Student, Subject, Semester, PointList

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(PointList)