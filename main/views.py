from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import SessionBeginDate,Student
from . import restApi


def starter(request):
    return render(request, 'main/starter.html')


def main(request):
    date1 = SessionBeginDate.objects.all()[0].date
    # if SessionBeginDate.DoesNotExist():
    #     date1 = datetime.datetime.now()
    return render(request, 'main/main.html', {"date": date1})


def cabinet(request):
    if (request.user.is_authenticated):
        if (request.user.is_superuser):
            return render(request, 'main/lkA.html')
            # return HttpResponseRedirect('/admin')
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
    return restApi.pointGraphDataJson(request, studentR, subjectR)


def lessonGraphData(request, groupR):
    return restApi.lessonGraphDataJson(request, groupR)


def lastSessionData(request, studentR):
    return restApi.lastSessionDataJson(request, studentR)


def resData(request):
    return restApi.resDataJson(request)

def adminStudentCabinet(request, studentR):
    if(request.user.is_superuser):
        return render(request, 'main/lk.html', {"student": Student.objects.get(pk=studentR)})
    else:
        return HttpResponseForbidden("You are not admin")


def studentsTopData(request, subjectR):
    return restApi.studentsTopDataJson(request, subjectR)

def surnameSearchData(request, surnameR):
    return restApi.surnameSearchJson(request, surnameR)