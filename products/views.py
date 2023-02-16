from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from products.filters import HouseFilter
from products.serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 500



class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HouseFilter


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'


class Oasdsf(ProductDetailAPIView):
    queryset = Product.objects.all().order_by('?')
    serializer_class = ProductSerializer


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


class ProductSimilar(APIView):
    def get(self, request, *args, **kwargs):
        home = Product.objects.get(id=kwargs['pk'])
        similar_price = Product.objects.filter(price=home.price)
        similar_area = Product.objects.filter(area_id=home.area_id)
        similar_square = Product.objects.filter(square=home.square)
        data_ = {
            "similar_price": ProductSerializer(similar_price, many=True).data,
            "similar_area": ProductSerializer(similar_area, many=True).data,
            "similar_square": ProductSerializer(similar_square, many=True).data,
        }
        return Response(data=data_)
