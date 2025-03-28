from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

import schedule
import time


def send_daily_summary():
    print('fui chamado')

schedule.every(10).seconds.do(send_daily_summary)


#while True:
#    schedule.run_pending()
#    time.sleep(1)


def email_html(path_template: str, assunto: str, para: list, **kwargs) -> dict:
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}