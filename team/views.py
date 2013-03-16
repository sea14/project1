# Create your views here.
from django.shortcuts import render
from team.models import Teams, Member
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	context = {
	'member_count': Member.objects.count(),
	'team_count': Teams.objects.count(),
}
	return render(request, "team/home.html", context)

def member(request, pk):
	member = Member.objects.all()
	#member = get_object_or_404(Member, id=pk)
	return render(request, "team/member.html", {'member': member})

def teams(request, pk):
	teams = get_object_or_404(Teams, id=pk)
	return render(request, "team/teams.html", {'teams': teams})

def teamsList(request):
	teams_list = Teams.objects.all()
	return render(request, 'team/teamsList.html', {"teams": teams})

def memberList(request):
	member_List = member.objects.all()
	return render(request, 'team/member_list.html', {"members": members})
