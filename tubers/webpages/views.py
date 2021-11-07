from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider, Team
from youtubers.models import Youtuber

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.filter(is_featured=True)
    all_youtubers = Youtuber.objects.all()
    data = {
        'sliders' : sliders,
        'teams' : teams,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def contact(request):
    return render(request, 'webpages/contact.html')

def services(request):
    return render(request, 'webpages/services.html')

