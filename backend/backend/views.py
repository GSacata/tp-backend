from django.shortcuts import render

def get_home_page(request):
    return render(request, "backend/main_templates/home.html")