from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.starter),
    path('starter', views.starter),
    path('main', views.main),
    path('cabinet', views.cabinet),
    path('login', views.loginUser),
    path('logout', views.logoutUser),
    url(r'^graphrestapi/(?P<studentR>[0-9]+)_(?P<subjectR>[0-9]+)/$', views.pointGraphData),
    url(r'^graphrestapi/(?P<groupR>[0-9]+)/$', views.lessonGraphData),
    url(r'^graphrestapi/last/(?P<studentR>[0-9]+)/$', views.lastSessionData),
    path('graphrestapi/res/', views.resData),
    url(r'^cabinet/(?P<studentR>[0-9]+)/$', views.adminStudentCabinet),
    url(r'^graphrestapi/top/(?P<subjectR>[0-9]+)/$', views.studentsTopData),
    url(r'^graphrestapi/search/(?P<surnameR>[a-z]+)$', views.surnameSearchData)
]
