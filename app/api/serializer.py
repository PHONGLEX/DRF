from rest_framework import serializers
from app.models import CarSpecs


class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = "__all__"
        depth = 1