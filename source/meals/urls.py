from django.urls import path
from .views import MealView

urlpatterns = [
    path('meals/', MealView.as_view(), name='meals'),
]
