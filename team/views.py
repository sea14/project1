# Create your views here.
from django.shortcuts import render
from team.models import Teams, Member
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
        context = {
        'memberCount': Member.objects.all(),
        'teamsInfo': Teams.objects.all(),
        'memberNumber': Member.objects.count(),
}
        return render(request, "team/home.html", context)

def member(request, pk):
	member = get_object_or_404(Member, id=pk)
	return render(request, "team/member.html", {'member': member})

def teams(request, pk):
        teams = get_object_or_404(Teams, id=pkd)
        return render(request, "team/team.html", {'teams': teams})

def teams(request):
    context = {
        'memberCount': Member.objects.all(),
        'teamsInfo' : Teams.objects.all(),
    }
    return render (request, "team/team.html", context)
