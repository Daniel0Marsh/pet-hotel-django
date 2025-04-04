from django.urls import path
from .views import TransportationView

urlpatterns = [
    path('transportation/', TransportationView.as_view(), name='transportation'),
]
