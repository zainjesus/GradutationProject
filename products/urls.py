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
    path('apartament/', ApartmentView.as_view()),
    path('apartament/<int:id>/', ApartmentDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('create/', Creating_Ad.as_view())
]