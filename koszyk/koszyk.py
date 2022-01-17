from decimal import Decimal
from django.conf import settings
from sklep.models import Product


class Koszyk(object):
    def __init__(self, request):
        """
        Inicjalizacja koszyka na zakupy.
        """

        self.session = request.session
        koszyk = self.session.get(settings.KOSZYK_SESSION_ID)
        if not koszyk:
            # Zapis pustego koszyka na zakupy w sesji.
            koszyk = self.session[settings.KOSZYK_SESSION_ID] = {}
        self.koszyk = koszyk

    def __iter__(self):
        """
         Iteracja przez elementy koszyka na zakupy i pobranie produktów z bazy danych.
         """
        product_ids = self.koszyk.keys()
        products = Product.objects.filter(id__in=product_ids)

        koszyk = self.koszyk.copy()
        for product in products:
            koszyk[str(product.id)]['product'] = product

        for item in koszyk.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['item'] * item['quantity']
            yield item

    def __len__(self):
        """
        Obliczenie liczby wszystkich elementów w koszyku na zakupy.
        """
        return sum(item['quantinty'] for item in self.koszyk.values())


    def add(self, product, quantity=1, update_quantity=False): #lub ovveride_quantity
        """
        Dodanie produktu do koszyka lub zmiana jego ilości.
        """
        product_id = str(product.id)
        if product_id not in self.koszyk:
            self.koszyk[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity: #tu tez
            self.koszyk[product_id]['quantity'] = quantity
        else:
            self.koszyk[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Oznaczenie sesji jako "zmodyfikowanej", aby upewnić się o jej zapisaniu.
        self.session.modified = True

    def remove(self, product):
        """
        Usunięcie produktu z koszyka na zakupy.
        """
        product_id = str(product.id)
        if product_id in self.koszyk:
            del self.koszyk[product_id]
            self.save()

    def clear(self):
        del self.session[settings.KOSZYK_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.koszyk.values())



