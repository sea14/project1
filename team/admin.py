#!/usr/bin/env python

from django.contrib import admin
from team.models import Member, Team

class MemberAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Member, MemberAdmin)

class TeamAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Team, TeamAdmin)
