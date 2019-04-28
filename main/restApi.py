from .models import Student, Subject, PointList, Lesson, AdditionalEduResource, ResourceToStudent
from django.http import JsonResponse
import random, sys

def pointGraphDataJson(request, studentR, subjectR):
    pointlist_data = []
    pointlist_labels = []
    subject_name = ""
    if(subjectR != 0):
        for pointlist in PointList.objects.order_by("semester").filter(student__id=studentR, subject__id=subjectR):
            pointlist_data.append(pointlist.point)
            pointlist_labels.append(str(pointlist.semester) + "й семестр")
        subject_name = "баллы по предмету " + Subject.objects.get(pk=subjectR).name
    else:
        pointlist_data = Student.objects.get(pk=studentR).semester_sorted_medium_points()
        i = 0
        while i < len(pointlist_data):
            pointlist_labels[i] = 1 + 'й семестр'
        subject_name = "средний балл"

    return JsonResponse({"datasets": [{"data": pointlist_data,
                                       "label": subject_name}],
                         "labels": pointlist_labels})


def lessonGraphDataJson(request, groupR):
    lessons_total = []
    lessons_passed = []
    lessons_labels = []
    i = 1
    for lesson in Lesson.objects.filter(group__id=groupR):
        lessons_total.append({"x": i, "y":lesson.total})
        lessons_passed.append({"x": i, "y":lesson.passed})
        lessons_labels.append(str(lesson.subject))
        i+=1
    return JsonResponse({"datasets": [{"data": lessons_total,"backgroundColor": '#4ab5c440',
                         "label": "всего пар"},
                                      {"data": lessons_passed, "backgroundColor": '#4ab5c470',
                                       "label": "прослушано пар"}],
    "labels": lessons_labels
})


def lastSessionDataJson(request, studentR):
    sem = list(Student.objects.get(pk=studentR).semester_sorted_pointlist_set().all())[-1].semester;
    points = Student.objects.get(pk=studentR).semester_sorted_pointlist_set().filter(semester=sem)
    pointlist_data = []
    pointlist_labels = []
    for p in points:
        pointlist_data.append(p.point)
        pointlist_labels.append(p.subject.name)
    return JsonResponse({"datasets": [{"data": pointlist_data,
                                       "label": "баллы за последнюю сессию"}],
                         "labels": pointlist_labels})


def resDataJson(request):
    res_data = []
    res_labels = []
    res_colors = []
    for res in AdditionalEduResource.objects.all():
        res_data.append(len(list(ResourceToStudent.objects.all().filter(resource=res))))
        res_labels.append(res.name)
        col = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        col += '32'
        res_colors.append(col)
    return JsonResponse({"datasets": [{"data": res_data,
                                       "label": "использование дополнительных образовательных ресурсов",
                                       "backgroundColor" : res_colors}],
                         "labels": res_labels})

def studentsTopDataJson(request, subjectR):
    last_sem = list(PointList.objects.filter(subject=Subject.objects.get(pk=subjectR)).order_by('semester'))[-1].semester
    points = PointList.objects.filter(subject=Subject.objects.get(pk=subjectR), semester=last_sem).order_by('point').reverse()
    top_data = []
    top_labels = []
    top_colors = []
    for p in points:
        top_data.append(p.point)
        top_labels.append(str(p.student) + (" (Вы)" if not request.user.is_superuser and not request.user.is_staff and
                                                      request.user.is_authenticated and p.student == request.user.student else ""))
        top_colors.append('#58918964')
    label = "Топ лучших студентов по предмету " + Subject.objects.get(pk=subjectR).name + " за последний семестр"
    return JsonResponse({"datasets": [{"data": top_data[:12],
                                       "label": label,
                                       "backgroundColor": top_colors}],
                         "labels": top_labels[:12]})

def surnameSearchJson(request, surnameR):
    studs = []
    lst = list(Student.objects.filter(surname__contains=surnameR)) + list(Student.objects.filter(name__contains=surnameR))
    for stud in lst:
        st = {"name": stud.name, "surname": stud.surname, "id": stud.pk}
        studs.append(st)
    return JsonResponse({"students": studs})