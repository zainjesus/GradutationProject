from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from users.models import Favorite


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=15)
    password = serializers.CharField(min_length=3)


class UserCreateSerializer(UserValidateSerializer):
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

