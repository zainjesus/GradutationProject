from rest_framework import serializers
from products.models import House, Category, Apartment


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = 'id price street floor category'.split()

class HouseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = 'id description price street category'.split()

class ApartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = 'id price street floor category'