import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
app = get_wsgi_application()  # Добавляем явное объявление app

# Для Vercel требуется переменная application
application = app