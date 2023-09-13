from rest_framework import serializers

from . import models

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = '__all__'

class SongnumberSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field='name', read_only = True)
    class Meta:
        model = models.Songnumber
        fields = ('number', 'album')

class SongSerializer(serializers.ModelSerializer):
    album = SongnumberSerializer(many = True, source = 'songnumber_set')

    class Meta:
        model = models.Song
        fields = ('name', 'album')