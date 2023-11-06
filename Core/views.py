from django.shortcuts import render,redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.http import HttpResponse 
import os
from .models import Post,URL,Contato,Email
from django.core.paginator import Paginator
from django.contrib.messages import constants
from django.contrib import messages
from Core.serializers import PostSerielizer
from django.core.exceptions import ObjectDoesNotExist

#@cache_page(60 * 15)
def index(request):
    posts_lista = Post.objects.filter(ativo=True).all().order_by('-data')
    pagina = Paginator(posts_lista, 10)
    page_number = request.GET.get('page')
    posts = pagina.get_page(page_number)
    return render(request,'index.html',{'posts':posts})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerielizer

def postid(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post.html',{'post':post,
                                        })
@cache_page(60 * 15)
def about(request):
    if request.method == "GET":
        return render(request,'about.html')

def contact(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request,'contact.html',{'status':status})
    else:
        NOME = request.POST.get('name')
        EMAIL = request.POST.get('email')
        TELEFONE = request.POST.get('phone')
        MENSAGEM = request.POST.get('message')
        
        new_contato= Contato(
            Nome=NOME,
            Email=EMAIL,
            Telefone=TELEFONE,
            Mensagem=MENSAGEM
        )
        new_contato.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect("/contact/?status=1")


@cache_page(60 * 15)
def redirecionar(request,link):
    try:
        links = URL.objects.get(short_link=link)
        return redirect(links.link_redirecionado)
    except ObjectDoesNotExist:
        return HttpResponse('Link não encontrado')
    

def formulario(request):
    if request.method =="POST":
        email = request.POST.get('email')
        valida = Email.objects.filter(email=email)
        if valida.exists():
            messages.add_message(request, constants.ERROR, 'Email Ja cadastrado')
            return redirect("/")
        cadastrar = Email.objects.create(
            email=email
        )
        cadastrar.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect("/")

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