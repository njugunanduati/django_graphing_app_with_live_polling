"""
WSGI config for polling_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

#import os
#
#from django.core.wsgi import get_wsgi_application
#
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
#
#application = get_wsgi_application()



import os
import django
from channels.routing import get_default_application
from channels.layers import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

channel_layer = get_channel_layer()

application = get_default_application()