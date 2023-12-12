from rest_framework.serializers import ModelSerializer
from .models import Task, TaskList


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskList
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"