from django.db import models

# Create your models here.
class CarPlan(models.Model):
    """Model definition for CarPlan."""
    plan_name = models.CharField(max_length=20)
    years_of_warranty = models.PositiveIntegerField(default=1)
    finance_plan = models.CharField(max_length=20, default="unavailable")

    def __str__(self):
        """Unicode representation of CarPlan."""
        return self.plan_name


class CarSpecs(models.Model):
    """Model definition for CarSpecs."""
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Unicode representation of CarSpecs."""
        return self.car_brand
