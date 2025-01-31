import os
import sys

# Update this path to point to your Django project root
path = '/home/nyarangi/WeatherApp/Weather_App_Django'
if path not in sys.path:
    sys.path.append(path)

# Update this to match your project's settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'WeatherApp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
