from django.urls import path
from .views import TaskAPIView, TaskListAPIView, OneTaskAPIView

urlpatterns = [
    path("tasks/", TaskAPIView.as_view(), name="get-all-tasks"),
    path("tasks/<int:pk>/", OneTaskAPIView.as_view(), name="get-task"),
    path("tasklist/", TaskListAPIView.as_view(), name="get-all-tasklists"),
]