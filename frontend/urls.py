from django.urls import path
from frontend import views


app_name = 'frontend'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('playlist/', views.playlist, name='playlist'),
    path('team/', views.team , name= 'team'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('details/', views.details, name='details'),
    path('tracks/', views.tracks, name='tracks'),
    path('albums/', views.albums, name='albums'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addsong/', views.add_song, name='addsong'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('editprofile/', views.edit_profile, name='edit')
]

