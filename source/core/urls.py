from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from branding.models import Branding

try:
    branding = Branding.objects.first()  # or get(id=1), if there's only one
    company_name = branding.company_name if branding else "Not Available"
except:
    company_name = "Not Available"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('hotel.urls')),
    path('', include('booking.urls')),
    path('', include('grooming.urls')),
    path('', include('transportation.urls')),
    path('', include('training.urls')),
    path('', include('water_sports.urls')),
    path('', include('meals.urls')),
    path('', include('contact.urls')),
    path('', include('about.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# configure admin titles
admin.site.site_header = f"welcome to {company_name} Admin"
admin.site.site_title = f"{company_name}"
admin.site.index_title = "Welcome to the admin area"
