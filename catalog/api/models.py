from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=30)
    artist = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album, through='Songnumber')

    def __str__(self):
        return self.name
    
class Songnumber(models.Model):
    number = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
