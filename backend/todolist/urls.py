from django.urls import path
from todolist.views import task_list, task_detail_change_delete

urlpatterns = [
    path('', task_list),
    path('<int:pk>/', task_detail_change_delete)
]