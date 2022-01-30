from celery import task
from django.core.mail import send_mail
from .models import Zamowienia

@task
def order_created(order_id):
    """
    Zadanie wysyłające powiadomienie za pomocą wiadomości e-mail
    po zakończonym powodzeniem utworzeniu obiektu zamówienia.
    """
    order = Zamowienia.objects.get(id=order_id)
    subject = 'Zamówienie nr {}'.format(order.id)
    message = 'Witaj, {}!\n\nZłożyłeś zamówienie w naszym sklepie.\
    Identyfikator zamówienia to {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent

