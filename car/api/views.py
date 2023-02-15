from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def cars_details(request):
    res = Car.objects.all()
    serializer = CarSerializer(res, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data , content_type ="application/json")

def car_detail(request,pk):
    res = Car.objects.get(id = pk)
    serializer = CarSerializer(res)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')
