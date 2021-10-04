from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user_name
    



    
class Team(models.Model):
    team_member_names = models.CharField(max_length=200)
    team_role = models.CharField(max_length=200)
    team_image = models.FileField(blank=True, null=True, upload_to='media/upload')
    profile = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.team_role
    
    class Meta():
        verbose_name_plural = 'Team'
        
    def get_team_img(self):
        return self.image
        
    def get_profile(self):
        
        return self.profile.url
        
        
class Album(models.Model):
    album_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Album')
    album_name = models.CharField(max_length=200)
    album_artist = models.CharField(max_length=200)
    number_of_tracks = models.PositiveIntegerField()
    album_genres = models.CharField(max_length=200, default=1)
    album_image = models.ImageField(blank=True, null=True, verbose_name='Album Image', upload_to='uploads/albums' )
    album_audio= models.FileField(blank=True, null=True, upload_to='upload')
    slug = models.SlugField(max_length=200)
    # user_id = models.ForeignKey(User, related_name='user_id',on_delete=models.CASCADE )
    approve = models.BooleanField(default=False)
    time_added = models.DateTimeField('date added', default=datetime.now())
    
    
    def __str__(self) :
        return self.album_name
    
    def get_album_image(self):
        if self.album_image:
            return self.album_image
        
        
    def get_album_audio(self):
        if self.album_audio:
            return self.album_audio
        
    def album_url(self):
        if self.album_name.url:
            return self.album_name.url
        else:
            return '/static/frontend/images/album_image'
        
    class Meta():
        verbose_name_plural = 'Album'
        
    def approve_album(self):   
        self.approve = True
        self.save()
        
class Track(models.Model):
    # track_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Track')
    track_name = models.CharField(max_length=200)
    track_artists = models.CharField(max_length=200)
    track_image = models.ImageField(blank=True, null=True, verbose_name='Track Image', upload_to ='uploads/tracks')
    # genre_name = models.ForeignKey(Genre, related_name='track_genre', on_delete=models.CASCADE, default=1)
    # user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    track_audio = models.FileField(blank=True, null=True, upload_to='upload')
    track_genre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    approve = models.BooleanField(default=False)
    
    
    def __str__(self) :
        return self.track_artists
    
    def get_track_name(self):
        if self.track_name:
            return self.track_name
        
    def get_track_audio(self):
        if self.track_audio:
            return self.track_audio
    
    
        
    class Meta():
        verbose_name_plural = 'Track'
                
    def approve_track(self):
        self.approve = True
        self.save()
        
    def __str__(self) :
        return self.track_name
    
    
    
class Genre(models.Model):
    genre_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Genre')
    genre_name = models.CharField(max_length=200)
    album_of_genres = models.ForeignKey(Album, related_name='genre_album', on_delete=models.CASCADE)
    track_of_genre = models.ForeignKey(Track, related_name='genre_track', on_delete=models.CASCADE)
    
  
        
    def get_album_genre(self):
        return self.album_of_genres
    
    def get_track_genre(self):
        return self.track_of_genre
        
    def __str__(self) :
        return self.genre_name
    
    
    
    
    
    
  
    
    
class Artist(models.Model):
    album_artist = models.ForeignKey(Album, related_name='artist_of_album', on_delete=models.CASCADE)
    track_artist = models.ForeignKey(Track, related_name='artist_of_track', on_delete=models.CASCADE)
    
    def get_album_artist(self):
        return self.album_artist
    
    def get_track_artist(self):
        return self.track_artist
    
    
    
    
