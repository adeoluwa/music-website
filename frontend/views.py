from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    return HttpResponse('<h1 style = "text-align: center; margin-top: 25%; font-weight : 900"> Welcome😃 </h>')

def playlist(request):
    return HttpResponse ('<h1 style = "text-align: center; margin-top: 25%; font-weight : 900"> Playlist🎵🎧 </h>')

def team(request):
    return HttpResponse('<h1 style = "text-align: center; margin-top: 25%; font-weight : 900"> Our Team👨‍👩‍👦‍👦 </h>')

def contact(request):
    return HttpResponse ('<h1 style = "text-align: center; margin-top: 25%; font-weight : 900"> Contact Us💌 </h>')

def login (request):
    return HttpResponse('<h1 style = "text-align: center; margin-top: 25%; font-weight : 900"> Protect your account 👁‍🗨 </h>')

def register(request):
    return HttpResponse ('<h1 style = "text-align: center; margin-top: 25%; font-weight : 900"> Join us 🚀 </h>')

