from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from products.models import Rooms, Product, Area, Type


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = 'title'.split()


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = 'title'.split()


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = 'title'.split()


class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    area = AreaSerializer()

    class Meta:
        model = Product
        fields = ('id', 'type', 'image', 'price', 'floor', 'area', 'square')

    def get_type_list(self, product_object):
        return [product_object.type.title]


class ProductDetailSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    area = AreaSerializer()
    rooms = RoomsSerializer()

    # warm_floor = serializers.SerializerMethodField()

    # living_space = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'type', 'area', 'rooms', 'image', 'price', 'phone_number', 'square', 'living_space',
            'ceiling_height', 'floor',
            'repair',
            'furniture', 'bathroom', 'window', 'warm_floor', 'balcony', 'description')


    # def get_warm_floor(self, obj):
    #     return (
    #         (1, 'Да'),
    #         (2, 'Нет')
    #     )[int(obj.warm_floor)][1]

    # def get_balcony_list(self, ):
    #     pass


class CreateAdSerializer(serializers.ModelSerializer):
    type_list = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'type_list', 'type', 'area', 'rooms', 'image', 'price', 'phone_number', 'square', 'living_space',
            'ceiling_height', 'floor',
            'repair',
            'furniture', 'bathroom', 'window', 'warm_floor', 'balcony', 'description')

    def get_type_list(self, product_object):
        return [product_object.type.title]


class ProductValidationSerializer(serializers.Serializer):
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    rooms = serializers.PrimaryKeyRelatedField(queryset=Rooms.objects.all())
    area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    phone_number = PhoneNumberField()
    price = serializers.IntegerField(max_value=1000000)
    square = serializers.CharField(max_length=15)
    living_space = serializers.CharField(max_length=500)
    ceiling_height = serializers.CharField(max_length=500)
    floor = serializers.IntegerField(max_value=6)
    repair = serializers.CharField(max_length=30)
    furniture = serializers.CharField(max_length=100)
    bathroom = serializers.CharField(max_length=50)
    window = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    warm_floor = serializers.CharField(default=1)
    balcony = serializers.CharField(default=1)