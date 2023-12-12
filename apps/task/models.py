from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class TaskList(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(_("Color"), max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Task List")
        verbose_name_plural = _("Task Lists")


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True, null=True)
    task_date = models.DateField(_("Task date"), default=timezone.now)
    task_time = models.TimeField(_("Task time"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    completed = models.BooleanField(_("Completed"), default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.task_time is None:
            self.task_time = timezone.now() + timezone.timedelta(hours=1)
        self.updated_at = timezone.now()
        super(Task, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
