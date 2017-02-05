import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/tricolourcare.com/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthnet.settings")

application = get_wsgi_application()
