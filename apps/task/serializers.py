from rest_framework.serializers import ModelSerializer
from .models import Task, TaskList


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskList
        fields = "__all__"
        read_only_fields = ['user']



class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['user']
