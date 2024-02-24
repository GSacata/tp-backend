from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from todolist.models import Task
from todolist.serializers import TaskSerializer
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)