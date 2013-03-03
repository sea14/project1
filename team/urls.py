# app urls team/urls.py
from django.conf.urls.defaults import patterns, url

from team import views

urlpatterns = patterns('',
	url(^$', views.home, name='team_home'),
	)
