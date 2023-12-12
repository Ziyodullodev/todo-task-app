from django.urls import path
from .views import TaskAPIView, TaskListAPIView

urlpatterns = [
    path("tasks/", TaskAPIView.as_view(), name="get-all-tasks"),
    path("tasklist/", TaskListAPIView.as_view(), name="get-all-tasklists"),
]