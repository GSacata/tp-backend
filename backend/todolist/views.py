# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.response import Response

# from todolist.models import Task
# from todolist.serializers import TaskSerializer
# # Create your views here.

# class TaskViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         queryset = Task.objects.all()
#         serializer = TaskSerializer(queryset, many=True)
#         return Response(serializer.data)

# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from todolist.models import Task
from todolist.serializers import TaskSerializer
...

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasklist = Task.objects.all()
        serializer = TaskSerializer(tasklist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            