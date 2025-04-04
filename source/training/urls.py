from django.urls import path
from .views import TrainingView

urlpatterns = [
    path('training/', TrainingView.as_view(), name='training'),
]
