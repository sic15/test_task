from django.contrib import admin

from .models import Album, Artist, Song, Songnumber

@admin.register(Artist)
class EcecutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'year']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Songnumber)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song', 'number', 'album']


