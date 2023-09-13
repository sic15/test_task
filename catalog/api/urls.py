from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import AlbumViewSet, ArtistViewSet, SongViewSet

router = SimpleRouter()
router.register('album', AlbumViewSet)
router.register('artist', ArtistViewSet)
router.register('song', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]