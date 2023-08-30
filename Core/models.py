from django.db import models
from django.db.models.fields import CharField
from django.utils.safestring import mark_safe


class ImagemTT(models.Model):
    imagens = models.ImageField(upload_to='twitter_img')

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.imagens}">'

    def __str__(self) -> str:
        return self.imagens.url

class Post(models.Model):
    headline = models.TextField(max_length=200)
    previa = models.TextField(max_length=200,null=True, blank=True)
    imagens =models.ManyToManyField (ImagemTT,null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    referencia = models.CharField(max_length=200,null=True, blank=True)
    por = models.CharField(max_length=50,null=True, blank=True)

    texto = models.TextField(max_length=500,null=True, blank=True)
    link  = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.headline