from django.urls import path
from products.views import *

list_create = {
    'get': 'list',
    'post': 'create'}

update_retrieve_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'}

urlpatterns = [
    path('house/', HouseView.as_view()),
    path('house/<int:id>/', HouseDetailView.as_view()),
    path('apartament/', HouseView.as_view())
]