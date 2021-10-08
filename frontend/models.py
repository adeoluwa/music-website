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
    
    # def __str__(self) :
    #     return self.team_role
    
    class Meta():
        verbose_name_plural = 'Team'
        
    def get_team_role(self):
        if self.team_role:
            return self.team_role
        
    def get_team_member_name(self):
        if self.team_member_names:
            return self.team_member_names
        
    def get_team_img(self):
        if self.team_image:
            return self.team_image.url
        
        
    def get_profile(self):
        if self.profile:
            return self.profile
        
        
class Album(models.Model):
    # album_id = models.OneToOneField(User, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    album_artist = models.CharField(max_length=200)
    number_of_tracks = models.PositiveIntegerField()
    album_genres = models.CharField(max_length=200, default=1)
    album_image = models.ImageField(blank=True, null=True, verbose_name='Album Image', upload_to='uploads/albums' )
    album_audio_1= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_2= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_3= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_4= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_5= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_6= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_7= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_8= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_9= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_10= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_11= models.FileField(blank=True, null=True, upload_to='upload')
    album_audio_12= models.FileField(blank=True, null=True, upload_to='upload')
    slug = models.SlugField(max_length=200, unique=True)
    # user_id = models.ForeignKey(User, related_name='user_id',on_delete=models.CASCADE )
    approve = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)
    time_added = models.DateTimeField('date added', default=datetime.now())
    
    
    def __str__(self) :
        return self.album_name
    
    def get_album_artist(self):
        if self.album_artist:
            return self.album_artist
        
    def get_album_genre(self):
        if self.album_genres:
            return self.album_genres
        
    def get_number_of_tracks(self):
        if self.number_of_tracks:
            return self.number_of_tracks
    
    def get_album_name(self):
        if self.album_name:
            return self.album_name
    
    def get_album_image(self):
        if self.album_image:
            return self.album_image.url
        
        
    def get_album_audio_1(self):
        if self.album_audio_1:
            return self.album_audio_1
        
    def get_album_audio_2(self):
        if self.album_audio_2:
            return self.album_audio_2
        
    def get_album_audio_3(self):
        if self.album_audio_3:
            return self.album_audio_3
        
    def get_album_audio_4(self):
        if self.album_audio_4:
            return self.album_audio_4
        
    def get_album_audio_5(self):
        if self.album_audio_5:
            return self.album_audio_5
        
    def get_album_audio_6(self):
        if self.album_audio_6:
            return self.album_audio_6
        
    def get_album_audio_7(self):
        if self.album_audio_7:
            return self.album_audio_7
        
    def get_album_audio_8(self):
        if self.album_audio_8:
            return self.album_audio_8
        
    def get_album_audio_9(self):
        if self.album_audio_9:
            return self.album_audio_9
        
    def get_album_audio_10(self):
        if self.album_audio_10:
            return self.album_audio_10
        
    def get_album_audio_11(self):
        if self.album_audio_11:
            return self.album_audio_11
        
    def get_album_audio_12(self):
        if self.album_audio_12:
            return self.album_audio_12
        
   
        
        
    def get_album_url(self):
        return reverse('public_view:album_name', kwargs={
            'slug': self.slug
        })
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
    slug = models.SlugField(max_length=200, unique=True)
    time_added = models.DateTimeField('date added', default=datetime.now())
    approve = models.BooleanField(default=False)
    
    
    def __str__(self) :
        return self.track_artists
    
    def get_track_artist(self):
        if self.track_artists:
            return self.track_artists
    
    def get_track_image(self):
        if self.track_image:
            return self.track_image.url
    
    def get_track_name(self):
        if self.track_name:
            return self.track_name
        
    def get_track_audio(self):
        if self.track_audio:
            return self.track_audio.url
    
    def get_track_url(self):
        return reverse('public_view:track_name', kwargs={
            'slug': self.slug
        })
        
    def get_time_added(self):
        if self.time_added:
            return self.time_added
    
        
    class Meta():
        verbose_name_plural = 'Track'
                
    def approve_track(self):
        self.approve = True
        self.save()
        
    # def __str__(self) :
    #     return self.track_name
    
    
    
    
class ContactUs(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    class Meta():
        verbose_name_plural = 'Contact Us'
    
    # def __str__(self):
    #     return self.n
    
    
    

    


    
    
    
