from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from frontend.models import *
from django.contrib import messages

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from frontend.forms import *
# from django import forms
#

# from django.http import HttpResponse
# Create your views here.

def home(request):
    track = Track.objects.filter().order_by('-time_added')[:4]
    album = Album.objects.filter().order_by('-time_added')[:4]
    context = {
        'track_key':track,
        'album_key':album
    }
    return render(request, 'frontend/index.html', context)



def team(request):
    team = Team.objects.order_by('-created')
    return render(request, 'frontend/team.html', {'members':team})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # user_email = 'kii-n-shi@outook.com'
        print(first_name,last_name,email,phone,message)
        # subject = 'Contact Form'
        # context = {
        #     'first_name': first_name,
        #     'last_name':last_name,
        #     'email':email,
        #     'phone':phone,
        #     'message':message
        # }
        # html_message = render_to_string('frontend/mail-template.html', context)
        # plain_message = strip_tags(html_message)
        # from_email= settings.FROM_EMAIL
        # send =  mail.send_mail(subject, plain_message, from_email,  html_message=html_message
        # )
        
        # if send:
            
        ContactUs.objects.create(first_name=first_name,last_name=last_name,email=email,phone=phone,message=message)
        messages.success(request, 'Message Sent')
        print('Success')
        # else:
        #     messages.error(request, 'Email not sent')
            
    return render(request, 'frontend/contact-us.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('frontend:dashboard')
        else:
            messages.error(request, 'Username and password incorrect')
    return render(request, 'frontend/login.html')
    


@login_required(login_url='/pages/login_view')
def logout_view(request):
    logout(request)
    return redirect('frontend:login_view')


def register(request):
    return render(request, 'frontend/register.html')


def details(request, slug):
    album_details = get_object_or_404(Album, slug=slug)
    return render(request, 'frontend/details.html', {'album':album_details})



def tracks(request):
    track = Track.objects.order_by('-time_added')
    return render(request, 'frontend/tracks.html', {'track':track})

def albums(request):
    album  = Album.objects.order_by('-time_added')
    return render(request, 'frontend/album.html', {'album':album})



@login_required(login_url='/dashboard/')
def dashboard(request):
    return render(request, 'frontend/Dashboard.html')




@login_required(login_url='/pages/login_view')
def add_album(request):
    if request.method == 'POST':
        album_form = AddAlbum(request.POST, request.FILES)
        if album_form.is_valid():
            album_form.save(commit=False)
            album_form.user = request.user
            album_form.instance.slug = album_form.cleaned_data.get('slug')
            album_form.save()
            messages.success(request, 'Album Added Successfully')
    else:
        album_form = AddAlbum()
            
    return render(request, 'frontend/AddSong.html' ,{'album_user':album_form})



@login_required(login_url='/pages/login_view')
def add_track(request):
    # if request.method == 'POST':
    #         track_form = AddTrack(request.POST)
    #         if track_form.is_valid(): 
    #             track_form.save()
    #             messages.success(request, 'Track Added Successfully')
    #     else:
    #         track_form = AddTrack  
    return render(request, 'frontend/Addsingle.html') #{'track':track_form})

@login_required(login_url='/pages/login_view')
def change_password(request):
    return render(request, 'frontend/changepwd.html')

