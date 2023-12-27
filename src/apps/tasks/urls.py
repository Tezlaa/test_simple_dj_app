from django.urls import path

from apps.tasks.views import ListTasks


urlpatterns = [
    path('', ListTasks.as_view())
]