from django.shortcuts import render
from django.utils import timezone
from .models import Post, Hackathon, Project, Team, UserTeamHack, UserTeamProject, UserTeam, User, UserRole

def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/base.html', {'posts': posts})

def login(request):
    return render(request, 'blog/login.html')

def home(request):
    temp = Project.objects.filter().order_by('-likes')
    hacks = Hackathon.objects.filter().order_by('date')
    projects = []
    counter = 0;
    for t in temp:
        projects.append(t)
        counter+=1
        if counter==9:
            break
    return render(request, 'blog/home.html', {'hacks': hacks, 'projects':projects})

def projects(request):
    temp = Project.objects.filter().order_by('-likes')
    hacks = Hackathon.objects.filter().order_by('date')
    projects = []
    counter = 0;
    for t in temp:
        projects.append(t)
        counter+=1

    return render(request, 'blog/projects.html',{'projects':projects})

def teams(request):
    teams = Team.objects.filter().order_by('created_date')
    count = 0
    return render(request, 'blog/teams.html', {'teams':teams, 'count':count})

def teamprof(request, team_id):
    team = Team.objects.get(id = team_id)
    projects = UserTeamProject.objects.filter(team=team_id)
    hacks = UserTeamHack.objects.filter(team=team_id)
    users =  UserTeam.objects.filter(team=team_id)
    return render(request, 'blog/teamprof.html', {'team':team, 'hacks':hacks, 'projects': projects, 'users': users})

def users(request):
    users = User.objects.filter()
    uroles = UserRole.objects.filter()
    return render(request, 'blog/teamprof.html', {'users': users, 'uroles':uroles})
