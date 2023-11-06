from django.db import models
from django.db.models.fields import CharField
from django.utils.safestring import mark_safe
import random
import string


class URL(models.Model):
    link_redirecionado = models.URLField()
    short_link = models.CharField(max_length=10,unique=True, blank=True)

    def generate_short_link(self):
        characters = string.ascii_letters + string.digits  # Letras e números
        return ''.join(random.choice(characters) for _ in range(10))  # Gera uma sequência de 10 caracteres

    def save(self, *args, **kwargs):
        if not self.short_link:  # Se o short_link ainda não foi definido
            self.short_link = self.generate_short_link()
            while URL.objects.filter(short_link=self.short_link).exists():  # Verifica se já existe um objeto com esse short_link
                self.short_link = self.generate_short_link()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_link

class Contato(models.Model):
    Nome = models.CharField(max_length=100,null=True, blank=True)
    Email = models.EmailField()
    Telefone = models.IntegerField()
    Mensagem = models.TextField(max_length=500)
    Lido = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Nome

class ImagemTT(models.Model):
    imagens = models.ImageField(upload_to='twitter_img')

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="{self.imagens.url}">'

    def __str__(self) -> str:
        return self.imagens.url

class Post(models.Model):
    headline = models.TextField(max_length=200)
    previa = models.TextField(max_length=200,null=True, blank=True)
    imagens =models.ManyToManyField (ImagemTT, blank=True)
    data = models.DateField(null=True, blank=True)
    referencia = models.CharField(max_length=200,null=True, blank=True)
    por = models.CharField(max_length=50,null=True, blank=True)

    texto = models.TextField(max_length=500,null=True, blank=True)
    link  = models.ForeignKey(URL, on_delete=models.CASCADE ,null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.headline
    
class Email(models.Model):
    email = models.EmailField()
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.email