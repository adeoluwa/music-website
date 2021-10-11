from django.urls import path
from frontend import views


app_name = 'frontend'

urlpatterns = [
    # path('home/', views.home, name='home'),
    # path('playlist/', views.playlist, name='playlist'),
    path('team/', views.team , name= 'team'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('details/<slug:slug>/', views.details, name='details'),
    path('tracks/', views.tracks, name='tracks'),
    path('albums/', views.albums, name='albums'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-album/', views.add_album, name='add-album'),
    path('add-track/', views.add_track, name='add-track'),
    path('change-password/', views.change_password, name='change-password'),
    
]

