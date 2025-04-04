from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


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
admin.site.site_header = "welcome to (Company name here) Admin"
admin.site.site_title = "Company name here"
admin.site.index_title = "Welcome to the admin area"
