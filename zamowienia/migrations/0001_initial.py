# Generated by Django 4.0.1 on 2022-01-23 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('adres', models.CharField(max_length=250)),
                ('kod_pocztowy', models.CharField(max_length=20)),
                ('miasto', models.CharField(max_length=100)),
                ('utworzono', models.DateTimeField(auto_now_add=True)),
                ('zaktualizowano', models.DateTimeField(auto_now=True)),
                ('platnosc', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='zamowienia.zamowienia')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='sklep.product')),
            ],
        ),
    ]
