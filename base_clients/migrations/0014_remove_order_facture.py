# Generated by Django 3.2.13 on 2022-06-14 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_clients', '0013_remove_order_prix_total_ttc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='facture',
        ),
    ]
