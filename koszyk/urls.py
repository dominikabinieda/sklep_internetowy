from django.urls import path
from . import views

app_name = 'koszyk'

urlpatterns = [
    path('', views.koszyk_wyswietl, name ='koszyk_wyswietl'),
    path('add/<int:product_id>/',
         views.koszyk_add, name='koszyk_add'),
    path('remove/<int:product_id>/',
         views.koszyk_remove, name = 'koszyk_remove'),
]