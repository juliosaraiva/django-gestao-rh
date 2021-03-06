from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail

from gestao_rh.apps.core.models import Company


@shared_task
def send_report():
    companies = Company.objects.count()
    return send_mail(
        'Celery Report', f'Total of Companies: {companies}',
        'contato@vespene.com.br', ['monitoring@vespene.com.br'],
        fail_silently=False
    )
