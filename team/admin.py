#!/usr/bin/env python

from django.contrib import admin
from team.models import Member, Teams

class MemberAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Member, MemberAdmin)

class TeamsAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Teams, TeamsAdmin)
