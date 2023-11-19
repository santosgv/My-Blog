from django.contrib import admin
from .models import Post,ImagemTT, URL,Contato,Email

@admin.action(description="Marcar como Lido")
def action_read_messenger(modeladmin,request,queryset):
    for mensagem in queryset:
        mensagem.Lido = True
        mensagem.save()
@admin.action(description="Marcar como Desativado")
def action_mark_false(odeladmin,request,queryset):
    for posts in queryset:
        posts.ativo=False
        posts.save()

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('Nome','Email','Telefone','Mensagem','Lido')
    readonly_fields=('Nome','Email','Telefone','Mensagem')
    list_filter = ('Lido',)
    actions = [action_read_messenger,]

@admin.register(URL)
class UrlAdmin(admin.ModelAdmin):
    list_display=('link_redirecionado','short_link',)
    readonly_fields=('short_link',)
    list_filter=('short_link',)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('headline','data','por','link')
    list_filter=('data','por','headline','link','ativo')
    actions=[action_mark_false,]

@admin.register(ImagemTT)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('icone','imagens')


admin.site.register(Email)