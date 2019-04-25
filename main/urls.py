from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.starter),
    url('starter', views.starter),
    url('main', views.main),
    url('cabinet', views.cabinet),
    url('login', views.loginUser),
    url('logout', views.logoutUser)
]
