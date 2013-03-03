# app urls team/urls.py
from django.conf.urls.defaults import patterns, url

from team import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='team_home'),
	#url(r'^team/$', views.teamList, name = 'team_team_list'),
	#url(r'^member/$', views.memberList, name = 'team_member_list'),
	url(r'^team/(?P<pk>\d+)$', views.team, name='team_team'),
	url(r'^member/(?P<pk>\d+)$', views.member, name='team_member'),
	)
