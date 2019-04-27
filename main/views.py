from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from .models import SessionBeginDate, PointList, Lesson, Subject, Student, AdditionalEduResource, ResourceToStudent


def starter(request):
    return render(request, 'main/starter.html')


def main(request):
    timediff = (SessionBeginDate.objects.all()[0].date - datetime.datetime.now())
    return render(request, 'main/main.html', {"session": SessionBeginDate.objects.all()[0],
                                              "time": datetime.datetime.now(),
                                              "timediff": timediff})


def cabinet(request):
    if (request.user.is_authenticated):
        if (request.user.is_superuser):
            return HttpResponseRedirect('/admin')
        else:
            return render(request, 'main/lk.html', {"student": request.user.student})
    else:
        return redirect('/login')


def loginUser(request):
    if (request.method == 'POST'):
        loginn = request.POST['login']
        password = request.POST['pswd']
        user = authenticate(request, username=loginn, password=password)
        if (user is not None):
            login(request, user)
            return redirect('/cabinet')
        else:
            return redirect('/main')
    else:
        return redirect('/main')


def logoutUser(request):
    logout(request)
    return redirect('/main')


def pointGraphData(request, studentR, subjectR):
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



def lessonGraphData(request, groupR):
    lessons_total = []
    lessons_passed = []
    lessons_labels = []
    colors_data = []
    i = 1
    for lesson in Lesson.objects.filter(subject__lesson__group_id=groupR):
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


def lastSessionData(request, studentR):
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


def resData(request):
    res_data = []
    res_labels = []
    for res in AdditionalEduResource.objects.all():
        res_data.append(len(ResourceToStudent.objects.all().filter(resource=res)))
        res_labels.append(res.name)
    return JsonResponse({"datasets": [{"data": res_data,
                                       "label": "использование дополнительных образовательных ресурсов"}],
                         "labels": res_labels})


def adminStudentCabinet(request, studentR):
    if(request.user.is_superuser):
        return render(request, 'main/lk.html', {"student": Student.objects.get(pk=studentR)})
    else:
        return HttpResponseForbidden("You are not admin")