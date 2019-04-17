from django.contrib import admin
from .models import Student, Subject, PointList, Group, AdditionalEduResource, Lesson, SessionBeginDate, ResourceToStudent

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(PointList)
admin.site.register(Group)
admin.site.register(AdditionalEduResource)
admin.site.register(Lesson)
admin.site.register(SessionBeginDate)
admin.site.register(ResourceToStudent)