import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourist_places_explorer.settings')
application = get_wsgi_application()
