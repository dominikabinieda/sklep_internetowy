from django.contrib import admin
from .models import Zamowienia, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Zamowienia)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie', 'nazwisko', 'email',
                    'adres', 'kod_pocztowy', 'miasto', 'platnosc',
                    'utworzono', 'zaktualizowano']
    list_filter = ['platnosc', 'utworzono', 'zaktualizowano']
    inlines = [OrderItemInline]



#admin.site.register(Zamowienia, OrderAdmin)
