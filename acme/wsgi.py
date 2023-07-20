"""
WSGI config for acme project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acme.settings')

application = get_wsgi_application()

# This application object is used by the development server
# as well as any WSGI server configured to use this file.

