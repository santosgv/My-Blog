import datetime
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
from .utils import email_html
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import logging

logger = logging.getLogger('MyApp')


def get_today_data():
    date_now  = datetime.datetime.now().date()
    return date_now

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

#@cache_page(60 * 15)
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
        return redirect("/contact/?status=1")

#@cache_page(60 * 15)
def redirecionar(request,link):
    try:
        links = URL.objects.get(short_link=link)
        return redirect(links.link_redirecionado)
    except ObjectDoesNotExist:
        logger.info(f'Link não encontrado '+str(datetime.datetime.now())+' horas!')
        return HttpResponse('Link não encontrado')
    

def formulario(request):
    if request.method =="POST":
        email = request.POST.get('email')
        valida = Email.objects.filter(email=email)
        if valida.exists():
            messages.add_message(request, constants.ERROR, 'Email Ja cadastrado')
            logger.info(f'Email Ja cadastrado {email} '+str(datetime.datetime.now())+' horas!')
            return redirect("/")
        cadastrar = Email.objects.create(
            email=email
        )
        cadastrar.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect("/")
    
def unsubscriber(request,id):
    email = Email.objects.get(id=id)
    email.ativo =False
    email.save()
    return HttpResponse('Cancelado sua Inscriçao')

@login_required(login_url='/admin/login/?next=/admin/') 
def enviar_emeil(request):
    try:
        path_template = os.path.join(settings.BASE_DIR, 'Core/templates/emails/email.html')
        base_url = request.build_absolute_uri('/')
        emails = Email.objects.filter(ativo=True).all()
        posts = Post.objects.all().filter(data=get_today_data()).order_by('-data')[:15]

        for email in emails:
            email_html(path_template, 'Novos Posts', [email,],posts=posts,email=email,base_url=base_url)
            messages.add_message(request, constants.SUCCESS, 'Emais enviados com sucesso')
            return redirect("/")
        
    except Exception as msg:
        messages.add_message(request, constants.ERROR, f'Nao foi possivel enviar os Emails consulte o arquivo de Log')
        logger.critical(f'{msg} '+str(datetime.datetime.now())+' horas!')
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

def ads(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'ads.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/ads.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
        
def my_links(request):
    return render(request,'my_links.html')


@csrf_exempt  # Para simplificar o exemplo (em produção, use proteção CSRF adequada)
def save_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = float(data['latitude'])
            longitude = float(data['longitude'])
            
            print(latitude,longitude)

            
            return JsonResponse({'status': 'success', 'message': 'Localização salva'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)