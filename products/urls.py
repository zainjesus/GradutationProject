from django.urls import path
from .views import *


urlpatterns = [
    path('products/<int:id>/', ProductDetailAPIView.as_view()),
    path('products', ProductListAPIView.as_view())
]