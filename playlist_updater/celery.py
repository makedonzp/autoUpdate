import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm3u_updater.settings')
app = Celery('m3u_updater')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()