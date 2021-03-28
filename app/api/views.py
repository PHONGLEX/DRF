from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from devtools import debug

from .serializer import CarSpecsSerializer
from app.models import CarSpecs, CarPlan


@api_view()
# @permission_classes([AllowAny])
def firstFunc(request):
    return Response({'message': "Hello World"})

@permission_classes([AllowAny])
class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs

    # override retrieve from ViewSet, since ModelViewSet is
    # inherited from ViewSet
    def retrieve(self, request, *args, **kwargs):
        print(request.user)
        params = kwargs
        print(params)
        cars = CarSpecs.objects.filter(car_brand=params['pk'])
        serializer = CarSpecsSerializer(cars, many=True)

        return Response(serializer.data)


    # override retrieve from ViewSet, since ModelViewSet is
    # inherited from ViewSet
    def create(self, request, *args, **kwargs):
        
        car_data = request.data
        print(car_data)
        new_car = CarSpecs.objects.create(car_brand=car_data['car_brand'],
        car_model=car_data['car_model'], production_year=car_data['production_year']
        ,car_body=car_data['car_body'], engine_type = car_data['engine_type']
        ,car_plan=CarPlan.objects.get(id=car_data['car_plan']))

        new_car.save()

        serializer = CarSpecsSerializer(new_car)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loggedin_user = request.user
        print(request)
        if loggedin_user == "admin":
            car = self.get_object()
            car.delete()
            message = {"message": "Item has been deleted"}
        else:
            message = {"message": "Not Allow"}

        return Response(message)
    
    
