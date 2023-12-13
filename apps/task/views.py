from .serializers import TaskSerializer, TaskListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .models import Task, TaskList
from rest_framework import status

# Create your views here.

class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TaskListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskListSerializer
    pagination_class = DefaultPagination
    search_fields = ['title',]
    filter_backends = (filters.SearchFilter,)
    
    def get_queryset(self):
        return TaskList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OneTaskListAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.filter(user=self.request.user)


class TaskAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    pagination_class = DefaultPagination

    search_fields = ['title', 'description', 'task_date']
    filter_backends = (filters.SearchFilter,)
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OneTaskAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)