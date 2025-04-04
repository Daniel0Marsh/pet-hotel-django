from django.urls import path
from .views import HotelView, ServicesView

urlpatterns = [
    path('hotel/', HotelView.as_view(), name='hotel'),
    path('services/', ServicesView.as_view(), name='services'),
]
