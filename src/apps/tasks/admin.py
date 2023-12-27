from django.contrib import admin

from apps.tasks.models import Task


@admin.register(Task)
class TaskAdminView(admin.ModelAdmin):
    list_display = ('title', 'priority', 'text')
    list_editable = ('text', 'priority')