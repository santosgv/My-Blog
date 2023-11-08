from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Contato
from django.core.mail import send_mail
from decouple import config

@receiver(post_save,sender=Contato)
def novo_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Email Recebido'
        message = f'''O Cliente {instance.Nome} enviou uma mensagem!
        {instance.Mensagem}
        '''
        from_email = config('EMAIL_HOST_USER')
        recipient_list = ['santosgomesv@gmail.com']
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return 'Super Usuario Criado'