# Generated by Django 3.2.13 on 2022-06-14 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_clients', '0008_auto_20220610_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prix_unitaire_TTC',
        ),
    ]
