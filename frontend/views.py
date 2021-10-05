from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from frontend.models import *

# Create your views here.

def home(request):
    return render(request, 'frontend/index.html')

def playlist(request):
    return render (request, 'frontend/playlist.html')

def team(request):
    team = Team.objects.order_by('-created')
    return render(request, 'frontend/team.html', {'members':team})

def contact(request):
    return render(request, 'frontend/contact-us.html')

def login(request):
    return render(request, 'frontend/login.html')

def register(request):
    return render(request, 'frontend/register.html')

def details(request):
    return render(request, 'frontend/details.html')


def tracks(request):
    track = Track.objects.order_by('-time_added')
    return render(request, 'frontend/tracks.html', {'track':track})

def albums(request):
    album  = Album.objects.order_by('-time_added')
    return render(request, 'frontend/album.html', {'album':album})

def dashboard(request):
    return render(request, 'frontend/Dashboard.html')

def add_album(request):
    return render(request, 'frontend/AddSong.html')

def add_track(request):
    return render(request, 'frontend/Addsingle.html')

def change_password(request):
    return render(request, 'frontend/changepwd.html')

def edit_profile(request):
    return render(request, 'frontend/edit.html')
