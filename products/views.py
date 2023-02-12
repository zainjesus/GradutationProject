from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from products.filters import HouseFilter
from products.serializers import *



class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HouseFilter


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'


class Create_AdView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateAdSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProductValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        product = Product.objects.create(**serializer.validated_data)
        product.save()
        return Response(data={'message': 'data received',
                              'personal_area': ProductValidationSerializer(product).data})