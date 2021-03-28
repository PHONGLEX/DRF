from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CarSpecsViewset


routers = DefaultRouter()
routers.register('car-specs', CarSpecsViewset, basename='car-specs')

urlpatterns = [
    path('first', views.firstFunc),
    path('', include(routers.urls))
]