from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:id>/', ProductDetailAPIView.as_view()),
    path('create/', Create_AdView.as_view())
]
