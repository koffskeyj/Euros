from django.shortcuts import render
from country_facts.models import Nation
from country_facts.models import AboutMe


def detailed_info_view(request):
    all_nations = Nation.objects.all()
    return render(request, 'detailed_info.html', {"nations": all_nations})


def home_view(request):
    return render(request, 'home.html')


def about_me_view(request):
    about_me = AboutMe.objects.all()
    return render(request, 'about_me.html', {"about": about_me})