from .serializers import TaskSerializer, TaskListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, TaskList
from rest_framework import status
from django.utils import timezone
# Create your views here.


class TaskListAPIView(APIView):
    
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            check_token = Token.objects.get(key=token).user
            if check_token:
                get_all_tasklists = TaskList.objects.filter(user=check_token)
                tasklist = TaskListSerializer(get_all_tasklists, many=True)
                return Response(
                    {
                        "status": "success",
                        "tasklists": tasklist.data,
                    }, status=status.HTTP_200_OK)
            
        return Response(
            {
                "status": "error",
                "message": "Invalid token",
            }, status=status.HTTP_400_BAD_REQUEST
        )
    def post(self, request):
        pass


class TaskAPIView(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            check_token = Token.objects.get(key=token).user
            if check_token:
                get_all_tasks = Task.objects.filter(user=check_token)
                task = TaskSerializer(get_all_tasks, many=True)
                return Response(
                    {
                        "status": "success",
                        "tasks": task.data,
                    }, status=status.HTTP_200_OK)
        return Response(
            {
                "status": "error",
                "message": "Invalid token",
            }, status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            check_token = Token.objects.get(key=token).user
            if check_token:
                data = {
                    "title": request.data.get("title"),
                    "user": check_token.id,
                    "description": request.data.get("description") or None,
                    "tasklist": request.data.get("tasklist") or None,
                    "task_date": request.data.get("task_date") or timezone.now(),
                    "task_time": request.data.get("task_time") or None,
                }
                serializer = TaskSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "status": "success",
                            "task": serializer.data,
                        }, status=status.HTTP_201_CREATED
                    )
                return Response(
                    {
                        "status": "error",
                        "errors": serializer.errors,
                    }, status=status.HTTP_400_BAD_REQUEST
                )

        return Response(
            {
                "status": "error",
                # "errors": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST
        )


class OneTaskAPIView(APIView):
    def get(self, request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            check_token = Token.objects.get(key=token).user
            if check_token:
                get_task = Task.objects.filter(user=check_token, pk=pk)
                if not get_task:
                    return Response(
                        {
                            "status": "error",
                            "message": "Task not found",
                        }, status=status.HTTP_404_NOT_FOUND
                    )
                task = TaskSerializer(get_task, many=True)
                return Response(
                    {
                        "status": "success",
                        "tasks": task.data,
                    }, status=status.HTTP_200_OK)
        return Response(
            {
                "status": "error",
                "message": "Invalid token",
            }, status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            check_token = Token.objects.get(key=token).user
            if check_token:
                task = Task.objects.filter(pk=pk).first()
                if task:

                    data = {
                        "title": request.data.get("title") or task.title,
                        "user": check_token.id,
                        "description": request.data.get("description") or task.description,
                        "task_date": request.data.get("task_date") or task.task_date,
                        "task_time": request.data.get("task_time") or task.task_time,
                    }
                    if request.data.get("task_list"):
                        data["task_list"] = request.data.get("task_list")
                    serializer = TaskSerializer(instance=task, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(
                            {
                                "status": "success",
                                "task": serializer.data,
                            }, status=status.HTTP_201_CREATED
                        )
                    return Response(
                        {
                            "status": "error",
                            "errors": serializer.errors,
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
                return Response(
                    {
                        "status": "error",
                        "message": "Task not found",
                    }, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {
                "status": "error",
                "message": "Invalid token",
            }, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            check_token = Token.objects.get(key=token).user
            if check_token:
                task = Task.objects.filter(pk=pk).first()
                if task:
                    task.delete()
                    return Response(
                        {
                            "status": "success",
                            "message": "Task deleted successfully",
                        }, status=status.HTTP_200_OK
                    )
                return Response(
                    {
                        "status": "error",
                        "message": "Task not found",
                    }, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {
                "status": "error",
                "message": "Invalid token",
            }, status=status.HTTP_400_BAD_REQUEST
        )