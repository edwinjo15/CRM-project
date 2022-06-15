from http import client
from django.db import models
from django.forms import DateTimeField

# Create your models here.

class Client(models.Model):
    GENRE=(
        ('F','feminin'),
        ('M','masculin'),
    )
    nom=models.CharField(max_length=50,null=True)
    prenom=models.CharField(max_length=50)
    sexe=models.CharField(max_length=1,choices=GENRE)
    date_naissance=models.DateField()
    adresse=models.CharField(max_length=250)
    code_postal=models.CharField(max_length=5)
    ville=models.CharField(max_length=100)
    telephone=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.prenom

class Product(models.Model):    
    CATEGORY = (
        ('Tricots', 'Tricots'),
        ('Couture', 'Couture'),
        ('Canevas', 'Canevas'),
        ('Machine à coudre', 'Machine à coudre')
        )
    nom=models.CharField(max_length=50)
    desciption=models.TextField(null=True)
    quantite_stock=models.PositiveIntegerField()
    prix_unitaire_HT=models.DecimalField(max_digits=5,decimal_places=2)


    def __str__(self):
        return self.nom

class Order(models.Model):
    STATUS_CHOICE=(
        ('attente','en attente expédition'),
        ('exp','expediée'),
        ('livr','livrée'),
    )
    produit=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantite=models.PositiveBigIntegerField()
    statut_commande=models.CharField(max_length=50,choices=STATUS_CHOICE)
    prix_total_HT=models.DecimalField(max_digits=5,decimal_places=2)
    client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)


# class OrderItem(models.Model):
#     client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)
#     produit=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
#     quantite=models.PositiveBigIntegerField()

class Promo(models.Model):
    remise=models.FloatField()
    duree_remise=models.DurationField()

    

