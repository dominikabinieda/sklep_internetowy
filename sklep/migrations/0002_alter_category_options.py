# Generated by Django 3.2.8 on 2022-01-17 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]