from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from .models import SessionBeginDate, PointList


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


def graphData(request, datatype):
    pointlist_data = []
    pointlist_labels = []
    for pointlist in PointList.objects.order_by("semester").filter(student__surname="Pupkin", subject__name="Algebra"):
        pointlist_data.append(pointlist.point)
        pointlist_labels.append(str(pointlist.semester) + "й семестр")
    return JsonResponse({"datasets": [{"data": pointlist_data,
                                       "label": "динамика успеваемости"}],
                         "labels": pointlist_labels})
