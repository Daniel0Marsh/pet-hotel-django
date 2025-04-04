from django.urls import path
from .views import GroomingView

urlpatterns = [
    path('grooming/', GroomingView.as_view(), name='grooming'),
]
