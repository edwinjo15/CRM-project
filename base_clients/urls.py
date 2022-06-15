"""GRETA_CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from base_clients.views import home,create_customer,create_product, orders_page,products_page,promotions_page,orderpage,delete_order

urlpatterns = [
        path('',home,name='index'),
        path('create_customer/', create_customer, name='create_customer'),        
        path('create_product/', create_product, name='create_product'),
        path('products_page/',products_page, name='page_produits'),
        path('promotions_page/',promotions_page, name='page_promotions'),
        path('order_page/',orders_page, name='orders_page'),
        path('orderpage/',orderpage, name='orderpage'),
        path('delete_order/', delete_order, name="delete_order"),
]