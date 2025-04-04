from django.urls import path
from .views import WaterSportsView

urlpatterns = [
    path('water-sports/', WaterSportsView.as_view(), name='water_sports'),
]
