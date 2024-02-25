# # function based
# from django.urls import path
# from todolist.views import task_list, task_detail_change_delete

# urlpatterns = [
#     # path('', task_list),
#     # path('<int:pk>/', task_detail_change_delete)
# ]

from django.urls import path
from todolist.views import TaskListAndCreate

urlpatterns = [
    path('', TaskListAndCreate.as_view())
]