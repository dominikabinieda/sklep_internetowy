from django.urls import path
from . import views
<<<<<<< HEAD
app_name = 'zamowienia'
urlpatterns = [
 path('create/', views.order_create, name='order_create'),
=======


app_name = 'zamowienia'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
>>>>>>> master
]