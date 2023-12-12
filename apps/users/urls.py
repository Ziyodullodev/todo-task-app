from .views import UserAPIView, LoginAPIView
from django.urls import path


urlpatterns = [
    path("users/<int:pk>/", UserAPIView.as_view(), name="get-all-users"),
    path("users/", UserAPIView.as_view(), name="get-all-users"),
    path("login/", LoginAPIView.as_view(), name="login"),

]