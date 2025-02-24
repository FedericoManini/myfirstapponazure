"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

settings_model = 'main.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'main.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_model)

port = int(os.environ.get("PORT", 8000))
os.environ.setdefault("DJANGO_RUNSERVER_PORT", str(port))

application = get_wsgi_application()
