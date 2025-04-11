from django.urls import path
from . import views

urlpatterns = [
    path('playlist.m3u', views.serve_playlist, name='serve_playlist'),
]