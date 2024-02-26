from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from todolist.models import Task

def get_home_page(request):
    return render(request, "backend/main_templates/home.html")

def get_bankview(request):
    taskbank = Task.objects.all().values()
    template = loader.get_template('backend/main_templates/bankview.html')
    context = {
        'taskbank': taskbank    
    }
    return HttpResponse(template.render(context, request))