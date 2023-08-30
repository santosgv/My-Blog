from django.contrib import admin
from .models import Post,ImagemTT, URL,Contato

admin.site.register(Contato)
admin.site.register(URL)
admin.site.register(Post)
admin.site.register(ImagemTT)