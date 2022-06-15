from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django.forms import ModelForm
from django import forms
from django.forms import ModelForm,TextInput,EmailInput,DateInput,Select
# from django.contrib.auth.forms import UserCreationForm
from .models import Client, Product, Order

class UploadForm(ModelForm):
    nom=forms.CharField(max_length=50)
    prenom=forms.CharField(max_length=50)
    sexe=forms.CharField(max_length=1)
    date_naissance=forms.DateField()
    adresse=forms.CharField(max_length=250)
    code_postal=forms.CharField(max_length=5)
    ville=forms.CharField(max_length=100)
    telephone=forms.CharField(max_length=10)
    email=forms.EmailField()
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'sexe', 'date_naissance', 'adresse', 'code_postal', 'ville', 'telephone', 'email']

class ProductForm(ModelForm):
    class Meta:
        model=Product
        widgets={
            'nom':TextInput(attrs={'class':'form-control'}),
            'description':TextInput(attrs={'class':'form-control'}),
            'quantite_stock':TextInput(attrs={'class':'form-control'}),
            'prix_unitaire_HT':TextInput(attrs={'class':'form-control'}),
        }
        fields="__all__"

class Form(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets={
                "produit":TextInput(attrs={'class': "form-control form-control-sm"}),
                "client":TextInput(attrs={'class': "form-control form-control-sm"}),
                "STATUS_CHOICE":TextInput(attrs={'class': "form-control form-control-sm"}),
                "quantite":TextInput(attrs={'class': "form-control form-control-sm"}),
                "prix_total_HT":TextInput(attrs={'class': "form-control form-control-sm"}),
                "statut_commande":TextInput(attrs={'class': "form-control form-control-sm"}),
                }  

