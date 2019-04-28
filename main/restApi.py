from .models import Student, Subject, PointList, Lesson, AdditionalEduResource, ResourceToStudent
from django.http import JsonResponse

def pointGraphDataJson(request, studentR, subjectR):
    pointlist_data = []
    pointlist_labels = []
    subject_name = ""
    if(subjectR != 0):
        for pointlist in PointList.objects.order_by("semester").filter(student__id=studentR, subject__id=subjectR):
            pointlist_data.append(pointlist.point)
            pointlist_labels.append(str(pointlist.semester) + "й семестр")
        subject_name = "баллы по предмету" + Subject.objects.get(pk=subjectR).name
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
    for res in AdditionalEduResource.objects.all():
        res_data.append(len(ResourceToStudent.objects.all().filter(resource=res)))
        res_labels.append(res.name)
    return JsonResponse({"datasets": [{"data": res_data,
                                       "label": "использование дополнительных образовательных ресурсов"}],
                         "labels": res_labels})

def studentsTopDataJson(request, subjectR):
    last_sem = list(PointList.objects.filter(subject=Subject.objects.get(pk=subjectR)).order_by('semester'))[-1].semester
    points = PointList.objects.filter(subject=Subject.objects.get(pk=subjectR), semester=last_sem).order_by('point').reverse()
    top_data = []
    top_labels = []
    for p in points:
        top_data.append(p.point)
        top_labels.append(str(p.student))
    label = "Топ лучших студентов по предмету " + Subject.objects.get(pk=subjectR).name + " за последний семестр"
    return JsonResponse({"datasets": [{"data": top_data,
                                       "label": label}],
                         "labels": top_labels})

def surnameSearchJson(request, surnameR):
    studs = []
    for stud in Student.objects.filter(surname__contains=surnameR):
        st = {"name": stud.name, "surname": stud.surname, "id": stud.pk}
        studs.append(st)
    return JsonResponse({"students": studs})