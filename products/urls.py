from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<int:id>/', ProductDetailAPIView.as_view())
]