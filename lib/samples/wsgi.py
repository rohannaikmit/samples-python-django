"""
WSGI config for samples project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


print("Starting development server")
sys.stdout.flush()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "samples.settings")
application = get_wsgi_application()
