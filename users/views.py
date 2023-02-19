import uuid
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from products.models import Product
from .models import Favorite
from .serializers import UserValidateSerializer, UserCreateSerializer, FavoriteSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .models import Profile
from .serializers import ProfileSer, ProfileUpdateSer, AvatarUpdateSer


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User be created!'},
                        status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'error': 'Incorrect login or password!'},
                        status=status.HTTP_401_UNAUTHORIZED)


class ProfileDetail(generics.RetrieveAPIView):
    """Профиль пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer


class ProfileUpdateView(generics.UpdateAPIView):
    """Редактирование профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer


class AvatarProfileUpdateView(generics.UpdateAPIView):
    """Редактирование аватара профилья пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = AvatarUpdateSer


class FavoriteAPIView(APIView):
    def get(self, request):
        # получить избранные продукты для пользователя или гостя
        if request.user.is_authenticated:
            favorites = Favorite.objects.filter(user=request.user)
        else:
            favorites = Favorite.objects.filter(session_key=request.session.session_key)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        # добавить продукт в избранное для текущего пользователя или гостя
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)
        if request.user.is_authenticated:
            favorite = Favorite.objects.create(user=request.user, product=product)
        else:
            session_key = request.session.session_key or uuid.uuid4().hex
            request.session['session_key'] = session_key
            favorite = Favorite.objects.create(session_key=session_key, product=product)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

