from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class GetGenres(APIView):
    def get(self, request):
        get_data = Genres.objects.all()
        ready_data = GenresSerializer(get_data, many=True).data

        return Response(ready_data)


class GetCitys(APIView):
    def get(self, request):
        get_data = City.objects.all()
        ready_data = CitysSerializer(get_data, many=True).data

        return Response(ready_data)


class GetWriters(APIView):
    def get(self, request):
        get_data = Writer.objects.all().select_related('city')
        print(get_data.query)
        ready_data = WritersSerializer(get_data, many=True).data
        # city = get_data.filter(city__name='Минск')
        # print(get_data.query)
        # print(get_data)
        # print(get_data[0].__dict__['_state'].fields_cache)
        # print(get_data[0].__dict__['_state'].fields_cache['city'].name, '-', get_data[0].__dict__['_state'].fields_cache['city'].info)
        # print(get_data[1].__dict__['_state'].fields_cache['city'].name, '-', get_data[1].__dict__['_state'].fields_cache['city'].info)
        # print(get_data[2].__dict__['_state'].fields_cache['city'].name, '-', get_data[2].__dict__['_state'].fields_cache['city'].info)
        return Response(ready_data)
# Create your views here.
