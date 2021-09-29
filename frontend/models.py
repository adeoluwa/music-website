from django.db import models
from  django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime
from django.utils.text import slugify  # django fuction to generate a slug automatically
from frontend.utils import random_string_generator








def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug=slugify(instance.title)

# Create your models here.


# class Artist(models.Model):
#     user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Artist')
#     user_name = models.CharField(max_length=200)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
    
#     def get_artist_name(self):
#         return self.user_name.capitalize()
    
#     def __str__(self) :
#         return self.name.capitalize()


class Genre(models.Model):
    genre_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Genre')
    genre_name = models.CharField(max_length=200)
    # user_id = models.ForeignKey( Artist, related_name='user_', on_delete=models.CASCADE)

    
    def get_genre_id(self):
        if self.genre_id:
            return self.genre_id
        
    def __str__(self) :
        return self.genre_name
    
class Team(models.Model):
    team_role = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.FileField(blank=True, null=True, upload_to='uploads')
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
    genre_name = models.ForeignKey(Genre, related_name='album_genre', on_delete=models.CASCADE, default=1)
    album_image = models.ImageField(blank=True, null=True, verbose_name='Album Image', upload_to='uploads/albums' )
    album_audio= models.FileField(blank=True, null=True, upload_to='upload')
    slug = models.SlugField(max_length=200)
    # user_id = models.ForeignKey(User, related_name='user_id',on_delete=models.CASCADE )
    approve = models.BooleanField(default=False)
    time_added = models.DateTimeField('date added', default=datetime.now())
    
    
    def __str__(self) :
        return self.album_image
    
    def get_album_name(self):
        if self.album_id:
            return self.album_name
        
    def get_album_audio(self):
        if self.album_id:
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
    track_artist = models.CharField(max_length=200)
    track_image = models.ImageField(blank=True, null=True, verbose_name='Track Image', upload_to ='uploads/tracks')
    genre_name = models.ForeignKey(Genre, related_name='track_genre', on_delete=models.CASCADE, default=1)
    # user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    track_audio = models.FileField(blank=True, null=True, upload_to='upload')
    slug = models.SlugField(max_length=200)
    approve = models.BooleanField(default=False)
    
    # def get_track_name(self):
    #     if self.track_name:
    #         return self.track_name
        
    def get_track_audio(self):
        if self.track_name:
            return self.track_audio
    
    # def get_track_artist(self):
    #     if self.track_artist:
    #         return self.track_artist
        
    class Meta():
        verbose_name_plural = 'Track'
                
    def approve_track(self):
        self.approve = True
        self.save()
        
    def __str__(self) :
        return self.track_name
    
    
