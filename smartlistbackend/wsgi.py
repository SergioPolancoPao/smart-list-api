"""
WSGI config for smartlistbackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from wsgiref.handlers import CGIHandler

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartlistbackend.settings')

application: CGIHandler = get_wsgi_application()
