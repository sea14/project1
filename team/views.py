# Create your views here.
from django.shortcuts import render
from team.models import Team, Member

def home(request):
	context = {
	'member_count': Member.objects.count(),
	'team_count': Team.objects.count(),
}
	return render(request, "base.html", context)

def member(request):
	member = Member.objects.order_by('?')[0]
	return render(request, "team/member.html", {'member': member})

def team(request):
	team = Team.objects.order_by('?')[0]
	return render(request, "team/team.html", {'team'; team})
