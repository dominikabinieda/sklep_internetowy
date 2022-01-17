from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from koszyk.koszyk import Koszyk


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
        return render(request,
                      'zamowienia/zamowienie/utworzone.html',
                      {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                    'zamowienia/zamowienie/utworz.html',
                    {'koszyk': koszyk, 'form': form})
