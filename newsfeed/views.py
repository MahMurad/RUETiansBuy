from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Ads

# Create your views here.


def home(request):
    context = {'ads': Ads.objects.all()}
    return render(request, 'newsfeed/home.html', context)


def about(request):
    return render(request, 'newsfeed/about.html', {'title': 'About'})

