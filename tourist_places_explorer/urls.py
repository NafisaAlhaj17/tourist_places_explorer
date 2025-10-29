from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # App routes
    path('', include('places.urls')),          # Home and place-related pages
    path('users/', include('users.urls')),     # Custom user features (if any)
    path('contact/', include('contact.urls')), # Contact page

    # Django built-in authentication (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),
]

# ✅ Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
