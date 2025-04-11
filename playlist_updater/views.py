
from django.http import FileResponse
import os

def serve_playlist(request):
    file_path = os.path.join(os.path.dirname(__file__), '../media/playlist.m3u')
    return FileResponse(open(file_path, 'rb'), content_type='text/plain')