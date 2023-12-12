from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status



class UserAPIView(APIView):
    def get(self, request):
        get_all_users = User.objects.all()
        users = UserSerializer(get_all_users, many=True)
        return Response(
            {
                "status": "success",
                "users": users.data,
            }, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass



class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {
                    "error": "Please provide both username and password"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        print(username, password)
        return Response({
            "status": "success",
            "message": "Login successful"
        }, status=status.HTTP_200_OK)
