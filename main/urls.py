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
    url(r'^graphrestapi/(?P<studentR>[0-9]*)_(?P<subjectR>[0-9]*)/$', views.pointGraphData),
    url(r'^graphrestapi/(?P<groupR>[0-9]*)/$', views.lessonGraphData)
]
