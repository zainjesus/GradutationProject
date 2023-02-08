from django.shortcuts import render
from rest_framework.response import Response
from products.serializers import *
from products.models import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView


class HouseView(ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetailView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
    lookup_field = 'id'

class ApartamentView(ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartamentSerializer

# @api_view(['GET'])
# def house_detail_view(request):
#     house = House.objects.get(id=id)
#     serializers = HouseDetailSerializer(house, many=True)
#     return Response(data=serializers.data)