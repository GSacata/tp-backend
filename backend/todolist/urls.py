from django.urls import path
from todolist.views import task_list

urlpatterns = [
    path('', task_list)
]