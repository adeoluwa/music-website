from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    return render(request, 'frontend/index.html')

def playlist(request):
    return render (request, 'frontend/playlist.html')

def team(request):
    return render(request, 'frontend/team.html')

def contact(request):
    return render(request, 'frontend/contact-us.html')

def login(request):
    return render(request, 'frontend/login.html')

def register(request):
    return render(request, 'frontend/register.html')

def details(request):
    return render(request, 'frontend/album-details.html')

def tracks(request):
    return render(request, 'frontend/tracks.html')



