import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourist_places_explorer.settings')
application = get_asgi_application()
