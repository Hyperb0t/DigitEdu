from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from .models import SessionBeginDate, PointList, Lesson


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
    for pointlist in PointList.objects.order_by("semester").filter(student__surname="Pupkin", subject__name="Algebra"):
        pointlist_data.append(pointlist.point)
        pointlist_labels.append(str(pointlist.semester) + "й семестр")
    return JsonResponse({"datasets": [{"data": pointlist_data,
                                       "label": "баллы по алгебре"}],
                         "labels": pointlist_labels})



def lessonGraphData(request, groupR):
    lessons_data = [];
    lessons_labels = [];
    for lesson in Lesson.objects.filter(group__name=groupR):
        lessons_data
    return JsonResponse({"datasets": [{"data": lessons_data,
                         "label": "прослушано пар"}],
    "labels": lessons_labels
})