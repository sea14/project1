# Create your views here.
from django.shortcuts import render
from team.models import Teams, Member
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
        context = {
        'memberCount': Member.objects.all(),
        'teamInfo': Teams.objects.all(),
}
        return render(request, "team/team.html", context)

def member(request, pk):
	member = get_object_or_404(Member, id=pk)
	return render(request, "team/member.html", {'member': member})

def teams(request):
    context = {
        'memberCount': Member.objects.all()
    }
    return render (request, "team/team.html", context)

#def teams(request, pk):
 #       teams = get_object_or_404(Teams, id=pk)
#return render(request, "team/teams.html", {'teams': teams})
#commenting out the below for now
#def memberList(request):
#	member_List = Member.objects.all()
#	return render(request, 'team/member_list.html', {"members": members})

#def teamsList(request):
#        teams_list = Teams.objects.get()
#       teams_list = teams_list.members.all()
#        #teamsList = get_object_or_404()
#        context = {
#            'memberList' : teams_list,
#            'teamsList' : teamsList,
#       }
        
#        return render (request, "team/teamsList.html", context)