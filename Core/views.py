from django.shortcuts import render
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.http import HttpResponse 
import os
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def postid(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post.html',{'post':post})

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')

@cache_page(60 * 15)
def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')