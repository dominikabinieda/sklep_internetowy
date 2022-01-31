from django import forms
from .models import Zamowienia

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Zamowienia
        fields = ['imie', 'nazwisko', 'email',
                     'adres', 'kod_pocztowy', 'miasto']


class SubscribeForm(forms.Form):
    email = forms.EmailField()