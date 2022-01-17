from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from koszyk.forms import KoszykAddProductForm
from koszyk.koszyk import Koszyk
from sklep_internetowy.sklep.models import Product


@require_POST
def koszyk_add(request, product_id):
    koszyk = Koszyk(request)
    product = get_object_or_404(Product, id=product_id)
    form = KoszykAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        koszyk.add(product=product,
                   quantity=cd['quantity'],
                   update_quantity=cd['update'])
        return redirect('koszyk:koszyk_wyswietl')

def koszyk_remove(request, product_id):
    koszyk = Koszyk(request)
    product = get_object_or_404(Product, id=product_id)
    koszyk.remove(product)
    return redirect('koszyk:koszyk_wyswietl')

def koszyk_wyswietl(request):
    koszyk = Koszyk(request)
    return  render(request, 'koszyk/szczegoly.html', {'koszyk':koszyk})