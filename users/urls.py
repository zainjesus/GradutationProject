from django.urls import path
from products import views
from users.views import LoginAPIView, RegistrationAPIView
from . import views
from users.views import LoginAPIView, RegistrationAPIView, FavoriteAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', LoginAPIView.as_view()),
    path("<int:pk>/", views.ProfileDetail.as_view()),
    path("update/<int:pk>/", views.ProfileUpdateView.as_view()),
    path("update/avatar/<int:pk>/", views.AvatarProfileUpdateView.as_view()),
    path('favorites/', FavoriteAPIView.as_view()),
]