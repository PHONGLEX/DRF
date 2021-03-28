from django.contrib import admin
from .models import CarSpecs, CarPlan

# Register your models here.
admin.site.register(CarSpecs)
admin.site.register(CarPlan)