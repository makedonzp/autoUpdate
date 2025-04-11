from django.db import models
import hashlib

class Playlist(models.Model):
    url = models.URLField(unique=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    checksum = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        self.checksum = hashlib.sha256(self.content.encode()).hexdigest()
        super().save(*args, **kwargs)