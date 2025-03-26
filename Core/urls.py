from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name ='Core'

urlpatterns = [
    path("", views.index, name='index'),
    path("post/<int:id>", views.postid, name='postid'),
    path("<str:link>",views.redirecionar, name ='redirecionar'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("formulario/", views.formulario, name='formulario'),
    path('enviar_emeil/',views.enviar_emeil, name='enviar_emeil'),
    path('unsubscriber/<int:id>',views.unsubscriber, name='unsubscriber'),
    path('my_links/',views.my_links, name='my_links'),
    path('save-location/', views.save_location, name='save_location'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)