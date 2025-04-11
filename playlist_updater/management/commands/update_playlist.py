import os
from django.core.management.base import BaseCommand
from playlist_updater.models import Playlist
from playlist_updater.utils import download_playlist, calculate_checksum
from django.utils import timezone


class Command(BaseCommand):
    help = 'Checks and updates playlist from GitHub'

    def handle(self, *args, **options):
        GITHUB_URL = 'https://gitlab.com/iptv135435/iptvshared/raw/main/IPTV_SHARED.m3u'

        new_content = download_playlist(GITHUB_URL)
        if not new_content:
            self.stdout.write(self.style.ERROR('Failed to download playlist'))
            return

        os.makedirs('media', exist_ok=True)  # Теперь эта строка будет работать

        with open('media/playlist.m3u', 'w', encoding='utf-8', errors='replace') as f:
            f.write(new_content)

        self.stdout.write(self.style.SUCCESS('Playlist updated successfully'))