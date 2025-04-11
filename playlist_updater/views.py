from django.http import FileResponse
from django.conf import settings
import os

def serve_playlist(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'playlist.m3u')
    return FileResponse(open(file_path, 'rb'), content_type='text/plain')