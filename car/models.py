from django.db import models

# Create your models here.
class Cars(models.Model):
    """Model definition for CarSpecs."""
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of CarSpecs."""
        return self.car_brand
