from .models import OrderItem
from .forms import OrderCreateForm
from koszyk.models import Koszyk

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse



def order_create(request):
    koszyk = Koszyk(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in koszyk:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Usunięcie zawartości koszyka na zakupy.
            koszyk.clear()
            # zmienna koszyk, jak nie działa to zmienić na plik koszyk
            #order_created.delay(order.id)
            if form.is_valid():
                subject = 'Twoje zamówienie zostało złożone'
                message = 'Dziękujemy za Twoje zamówienie w naszym sklepie.'
                recipient = form.cleaned_data.get('email')
                send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [recipient],
                          fail_silently=False)
                messages.success(request, 'Success!')
            return render(request,
                          'zamowienia/zamowienie/utworzone.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                    'zamowienia/zamowienie/utworz.html',
                    {'koszyk': koszyk, 'form': form})
