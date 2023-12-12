from .views import LoginAPIView, RegisterAPIView
from django.urls import path


urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),

]