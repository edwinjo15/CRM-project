# Generated by Django 3.2.13 on 2022-06-08 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_clients', '0002_rename_clients_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('desciption', models.TextField()),
                ('quantite_stock', models.PositiveIntegerField()),
                ('prix_unitaire_HT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prix_unitaire_TTC', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('quantite', models.PositiveBigIntegerField()),
                ('statut_commande', models.CharField(choices=[('attente', 'en attente expédition'), ('exp', 'expediée'), ('livr', 'livrée')], max_length=50)),
                ('prix_total_HT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prix_total_TTC', models.DecimalField(decimal_places=2, max_digits=5)),
                ('facture', models.FileField(upload_to='')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_clients.client')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_clients.product')),
            ],
        ),
    ]
