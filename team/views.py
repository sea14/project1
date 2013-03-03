# Create your views here.
from django.shortcuts import render
from team.models import Team, Member
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	context = {
	'member_count': Member.objects.count(),
	'team_count': Team.objects.count(),
}
	return render(request, "team/base.html", context)

def member(request, pk):
	#member = Member.objects.order_by('?')[0]
	course = get_object_or_404(Course, id=pk)
	return render(request, "team/member.html", {'member': member})

def team(request, pk):
	team = Team.objects.order_by('?')[0]
	team = get_object_or_404(Team, id=pk)
	return render(request, "team/team.html", {'team': team})