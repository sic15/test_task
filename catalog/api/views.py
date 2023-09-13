from rest_framework import viewsets 

from .models import Artist, Album, Song, Songnumber
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, SongnumberSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class Songnumber(viewsets.ModelViewSet):
    queryset = Songnumber.objects.all()
    serializer_class = SongnumberSerializer
