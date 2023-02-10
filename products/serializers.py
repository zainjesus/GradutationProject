from rest_framework import serializers
from products.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('type', 'area', 'rooms', 'image', 'square', 'living_space', 'ceiling_height', 'floor', 'repair',
                  'furniture', 'bathroom', 'window', 'warm_floor', 'balcony', 'description')


