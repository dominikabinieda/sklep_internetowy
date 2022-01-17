from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from sklep_internetowy.sklep.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from koszyk.forms import KoszykAddProductForm #Dodanie produktu do koszyka na zakupy


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})

#Dodanie produktu do koszyka na zakupy
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id,
                                slug=slug,
                                available=True)
    koszyk_produkt_form = KoszykAddProductForm()
    return render(request,
                  'sklep/produkty/szczegoly.html',
                  {'product': product,
                   'koszyk_product_form': koszyk_produkt_form})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]