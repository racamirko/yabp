from django.shortcuts import render
from models import *


def home(request):
    context = {'stories': Story.objects.order_by('-date')[:5]}
    return render(request, 'home.html', context)


def print_story(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'story.html', context={'story': story})


def show_tag(request, tag_id, tag_name):
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'tag.html', context={'tag':tag})