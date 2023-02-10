from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from products.filters import HouseFilter
from products.serializers import *


class HouseView(ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HouseFilter


class HouseDetailView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
    lookup_field = 'id'


class ApartmentView(ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartamentSerializer


class ApartmentDetailView(RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDetailSerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['category__title']


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class Creating_Ad(ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = Creating_Ad_Serializer
