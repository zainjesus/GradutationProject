from django.shortcuts import render
from rest_framework.response import Response
from products.serializers import *
from products.models import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView


class ProductView(ListAPIView):
    queryset = Product.objects.all()


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'