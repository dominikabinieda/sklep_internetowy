from celery import task
from django.core.mail import send_mail
from .models import Zamowienia


@task
def order_created(order_id):
    zamowienie = Zamowienia.objects.get(id=order_id)
    subject = f'Zamówienie nr. {zamowienie.id}'
    message = f'Drogi/Droga {zamowienie.first_name},\n\n' \
              f'Twoje zamówienie zostało zakończone.' \
              f'Numer Twojego zamówienia to {zamowienie.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'djangotestgangusy@gmail.com',
                          [zamowienie.email])
    return mail_sent