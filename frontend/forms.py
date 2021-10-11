from django import forms
from django.db.models import fields
from frontend.models import *


class AddAlbum(forms.ModelForm):
    album_name = forms.CharField()
    # album_audio = forms.FileField()
    
    class Meta():
        model = Album
        fields = '__all__' 
        exclude = ['slug', 'approve']
        
    def clean_name(self):
        album_name = self.clean_name.get('album_name').capitalize()
        if Album.objects.filter(album_name=album_name).exists():
            raise forms.ValidationError(f'{album_name} already exist')
        return album_name
    
    
# class AddTrack(forms.ModelForm):
#     track_audio = forms.FileField(
#         widget=forms.FileInput(attrs = {
#             'class': 'form-control',
#             'placeholder':'Add Song'
#         })
#     )
    
#     class Meta():
#         model = Track
#         fields =  '__all__'
        
#     def clean_name(self):
#         track_audio = self.clean_name.get('track_name').capitalize()
#         if Track.objects.filter(track_audio).exists():
#             raise forms.ValidationError(f'{track_audio} already exist')
#         return track_audio
    
    