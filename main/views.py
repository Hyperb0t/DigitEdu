from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from .models import SessionBeginDate

def starter(request):
    return render(request, 'main/starter.html')


def main(request):
    return render(request, 'main/main.html', {"session" : SessionBeginDate.objects.all()[0]})


def cabinet(request):
    if(request.user.is_authenticated):
        if(request.user.is_superuser):
            return HttpResponseRedirect('/admin')
        else:
            return render(request, 'main/cabinet.html', {"student":request.user.student})
    else:
        return HttpResponseRedirect('/login')


def loginUser(request):
    if(request.method == 'POST'):
        loginn = request.POST['login']
        password = request.POST['pswd']
        user = authenticate(request, username=loginn, password=password)
        if(user is not None):
            login(request, user)
            return redirect('cabinet/')
        else:
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/main')
