from celery import task, Celery
from django.core.mail import send_mail
from .models import Zamowienia

app = Celery('tasks', broker='amqp://guest:**@127.0.0.1:5672//')

@task
def order_created(order_id):
    order = Zamowienia.objects.get(id=order_id)
    subject = f'Zamówienie nr. {order.id}'
    message = f'Drogi/Droga {order.first_name},\n\n' \
              f'Twoje zamówienie zostało zakończone.' \
              f'Numer Twojego zamówienia to {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'djangotestgangusy@gmail.com',
                          [order.email])
    return mail_sent