from django.shortcuts import render
from models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')

def print_story(request, id):
    # return render(request, 'home.html')