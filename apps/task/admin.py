from django.contrib import admin
from .models import Task, TaskList
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at", "updated_at", "completed"]
    list_filter = ["user", "created_at", "updated_at", "completed"]
    search_fields = ["title", "user", "created_at", "updated_at", "completed"]
    list_editable = ["completed"]


class TaskListAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at"]
    list_filter = ["user", "created_at"]
    search_fields = ["title", "user", "created_at"]
    list_editable = []


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
