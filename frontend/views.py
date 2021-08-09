from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    return HttpResponse('home page')

def playlist(request):
    return HttpResponse ('playlist')

def team(request):
    return HttpResponse('Our team')

def contact(request):
    return HttpResponse ('contact us')

def login (request):
    return HttpResponse('login')

def register(request):
    return HttpResponse ('register')

