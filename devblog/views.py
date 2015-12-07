from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from models import *


def home(request):
    context = {'stories': Story.objects.order_by('-date')[:5]}
    return render(request, 'home.html', context)

def ajax_get_more_stories(request, story_offset, num_stories):
    story_offset = int(story_offset) # TODO: this can be handled in the urls.py, check documentation
    num_stories = int(num_stories)
    context = {'stories': Story.objects.order_by('-date')[story_offset:story_offset+num_stories]}
    return render(request, 'vanila_ajax_return.html', context)

def print_story(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'story.html', context={'story': story})

def show_tag(request, tag_id, tag_name):
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'tag.html', context={'tag':tag})

def login_form(request):
    return render(request, 'login_form.html')

def login_procedure(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect("/") # for now
        else:
            return redirect("/vrata/?err=1")
    else:
        return redirect("/vrata/?err=2")

def logout_procedure(request):
    pass
    # if request.user.is_authenticated():
