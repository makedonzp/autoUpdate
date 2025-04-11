from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from playlist_updater.views import serve_playlist

urlpatterns = [
    path('playlist.m3u', serve_playlist),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
