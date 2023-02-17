from django.urls import path
from users.views import LoginAPIView, RegistrationAPIView, FavoriteAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', LoginAPIView.as_view()),
    path('favorites/', FavoriteAPIView.as_view()),
]