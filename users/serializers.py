from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
from django.contrib.auth.models import User

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


class UserSer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("username", "email")


class ProfileSer(serializers.ModelSerializer):
    """Профиль пользователя"""
    user = UserSer()

    class Meta:
        model = Profile
        fields = ("user", "avatar", "email", "phone", "first_name", "last_name")


class ProfileUpdateSer(serializers.ModelSerializer):
    """Редактирование профиля пользователя"""

    class Meta:
        model = Profile
        fields = ("avatar", "email", "phone", "first_name", "last_name")


class AvatarUpdateSer(serializers.ModelSerializer):
    """Редактирование аватар ользователя"""

    class Meta:
        model = Profile
        fields = ("profile_pic",)


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = 'user product'.split()

