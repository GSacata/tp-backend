# # function based
# from django.urls import path
# from todolist.views import task_list, task_detail_change_delete

# urlpatterns = [
#     # path('', task_list),
#     # path('<int:pk>/', task_detail_change_delete)
# ]

from django.urls import path
from todolist.views import TaskListAndCreate, TaskDetailUpdateAndDelete, get_todolist_all, get_todolist_detail

# urlpatterns = [
#     path('', TaskListAndCreate.as_view()),
#     path('<pk>/', TaskDetailUpdateAndDelete.as_view())
# ]

urlpatterns = [
    path('', get_todolist_all),
    path('<pk>/', get_todolist_detail),
]