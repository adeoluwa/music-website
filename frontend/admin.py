from django.contrib import admin
from frontend.models import *
admin.site.site_header = '8th Realm Music'

# Register your models here.
# admin.site.register(Artist)
# admin.site.register(Album)
admin.site.register(Team)
# admin.site.register(Track)
# admin.site.register(Genre)

@admin.register(Album)
class Albumadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('album_name',)}
    
@admin.register(Track)
class Trackadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('track_name',)}
    
