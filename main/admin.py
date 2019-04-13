from django.contrib import admin
from .models import Student, Subject, Semester, PointList, Group, AdditionalEduResource, Lessons, SessionBeginDate

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(PointList)
admin.site.register(Group)
admin.site.register(AdditionalEduResource)
admin.site.register(Lessons)
admin.site.register(SessionBeginDate)