# app urls team/urls.py
from django.conf.urls.defaults import patterns, url

from team import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='team_home'),
	url(r'^teams/$', views.teams, name = 'team_teams'),
	#url(r'^member/$', views.memberList, name='team_member_list'),
	#url(r'^teams/(?P<pk>\d+)$', views.teams, name='team_teams'),
	url(r'^member/(?P<pk>\d+)$',views.member, name='teams_member'),
	)
