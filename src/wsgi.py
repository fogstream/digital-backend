"""
Конфигурация WSGI для digital_backend.

Больше информации:
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'digital_backend.settings.prod'
)

# pylint: disable=invalid-name
application = get_wsgi_application()
