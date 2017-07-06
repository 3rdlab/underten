#from django.contrib.auth.views import login, logout

from django.contrib.auth import views as auth_views

from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
	url(r'login/$', views.user_login),
	url(r'login_form/$', views.login_form),
	url(r'logout/$', views.user_logout),
	url(r'register/$', views.user_register),
)
