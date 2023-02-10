from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<int:id>/', ProductDetailDeleteAPIView.as_view())
]