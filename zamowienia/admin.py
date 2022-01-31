from django.contrib import admin
from .models import Zamowienia, OrderItem
import csv
import datetime
from django.http import HttpResponse


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Zapis pierwszego rekordu wraz z informacjami nagłówka.
    writer.writerow([field.verbose_name for field in fields])
    # Zapis rekordów danych.
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Eksport do CSV'

@admin.register(Zamowienia)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie', 'nazwisko', 'email',
                    'adres', 'kod_pocztowy', 'miasto', 'platnosc',
                    'utworzono', 'zaktualizowano']
    list_filter = ['platnosc', 'utworzono', 'zaktualizowano']
    inlines = [OrderItemInline]
    actions = [export_to_csv]



#admin.site.register(Zamowienia, OrderAdmin)
