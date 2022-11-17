from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json


# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def profile(request):
    return render(request, 'core/profile.html')