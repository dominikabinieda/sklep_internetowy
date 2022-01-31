#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from rest_framework import permissions
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from koszyk.forms import KoszykAddProductForm  # Dodanie produktu do koszyka na zakupy
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Category

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'sklep/produkty/lista.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


# Dodanie produktu do koszyka na zakupy
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug,
                                available=True)
    koszyk_produkt_form = KoszykAddProductForm()

    return render(request,
                  'sklep/produkty/szczegoly.html',
                  {'product': product,
                   'koszyk_product_form': koszyk_produkt_form})


class OrganizationAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    #serializer_class = serializer.OrganizationSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True,
                         "message": "Organization Added !",
                         "data": serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)
