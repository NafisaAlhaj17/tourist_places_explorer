from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    #  Redirect the home page to the main places list
    path('', RedirectView.as_view(pattern_name='places:place_list', permanent=False)),

    # ⚙️ Admin panel
    path('admin/', admin.site.urls),

    #  App routes
    path('places/', include('places.urls')),      # Tourist places pages
    path('users/', include('users.urls')),        # User signup/login/logout
    path('contact/', include('contact.urls')),    # Contact form

    # 🔐 Django built-in authentication
    path('accounts/', include('django.contrib.auth.urls')),
]

#  Serve uploaded media files (only in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
