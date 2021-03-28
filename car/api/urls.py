from django.urls import path
from .views import CarsAPIView

urlpatterns = [
    path('cars', CarsAPIView.as_view())
]