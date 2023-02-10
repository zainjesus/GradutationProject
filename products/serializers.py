from rest_framework import serializers

from products.models import House, Category, Apartment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = 'id category_list price street floor '.split()

    def get_category_list(self, house_object):
        return [i.title for i in house_object.category.all()]


class HouseDetailSerializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = 'id category_list description price street '.split()

    def get_category_list(self, house_object):
        return [i.title for i in house_object.category.all()]


class ApartamentSerializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = 'id category_list price street floor'.split()

    def get_category_list(self, house_object):
        return [i.title for i in house_object.category.all()]


class ApartmentDetailSerializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = 'id category_list price street floor'.split()

    def get_category_list(self, house_object):
        return [i.title for i in house_object.category.all()]


class Creating_Ad_Serializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = 'price street category_list category rooms floor description'.split()

    def get_category_list(self, house_object):
        return [i.title for i in house_object.category.all()]