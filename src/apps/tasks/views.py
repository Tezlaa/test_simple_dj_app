from django.views.generic import ListView

from apps.tasks.models import Task


class ListTasks(ListView):
    template_name = 'tasks/index.html'
    model = Task