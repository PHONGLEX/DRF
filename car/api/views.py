from rest_framework.views import APIView
from .serializer import CarsSerializer
from car.models import Cars
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

@permission_classes([AllowAny])
class CarsAPIView(APIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id is not None:
                car = Cars.objects.get(id=id)
                serializer = CarsSerializer(car)
                return Response(serializer.data)
        except:
            cars = self.get_queryset()

            serializer = CarsSerializer(cars, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_data = request.data
        car = Cars.objects.create(car_brand=car_data['car_brand'],
        car_model=car_data['car_model'], production_year=car_data['production_year']
        , car_body=car_data['car_body'], engine_type=car_data['engine_type'])

        car.save()

        serializer = CarsSerializer(car)
        return Response(serializer.data)
