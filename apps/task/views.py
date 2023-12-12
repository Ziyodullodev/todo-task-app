from .serializers import TaskSerializer, TaskListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, TaskList
from rest_framework import status
# Create your views here.


class TaskListAPIView(APIView):
    def get(self, request):
        get_all_tasklists = TaskList.objects.all()
        tasklist = TaskListSerializer(get_all_tasklists, many=True)
        return Response(
            {
                "status": "success",
                "tasklists": tasklist.data,
            }, status=status.HTTP_200_OK)
    def post(self, request):
        pass


class TaskAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


