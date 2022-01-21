from django.db import models
from sklep.models import Product


class Zamowienia(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField()
    adres = models.CharField(max_length=250)
    kod_pocztowy = models.CharField(max_length=20)
    miasto = models.CharField(max_length=100)
    utworzono = models.DateTimeField(auto_now_add=True)
    zaktualizowano = models.DateTimeField(auto_now=True)
    platnosc = models.BooleanField(default=False)

<<<<<<< HEAD

class Meta:
    ordering = ('-created',)

    def __str__(self):

        return 'Order {}'.format(self.id)

    def get_total_cost(self):

=======
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
>>>>>>> origin/master
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
<<<<<<< HEAD
    order = models.ForeignKey(Zamowienia, related_name='items',
=======
    order = models.ForeignKey(Zamowienia,
                              related_name='items',
>>>>>>> origin/master
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
<<<<<<< HEAD

        return '{}'.format(self.id)

    def get_cost(self):

=======
        return str(self.id)

    def get_cost(self):
>>>>>>> origin/master
        return self.price * self.quantity
