from email import message
from http import client
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
# from djangouploads.models import 
from .models import Client, Product, Order
from .forms import UploadForm, ProductForm, Form
# Create your views here.


def home(request):
    client = Client.objects.all()
    return render(request,'base_clients/index.html',  {'Client_list':client})

def create_customer(request):
    if request.POST:
        form = UploadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'base_clients/create_customer.html', {'form': UploadForm})

def create_product(request):
    produits=Product.objects.all()
    product_form=ProductForm()
    context={'formulaire_creation_produit':product_form,
                'liste_produits':produits
        }
    if request.method=="POST":
        product_form=ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
        return redirect('page_produits')
    return render(request,"base_clients/create_product.html",context)


def orders_page(request):
        orderform = Order.objects.all()
        form = Form()
        context={'formulaire_creation_order':form,
                'liste_produits':orderform
        }
        if request.method == 'POST':
                form = Form(request.POST)
                if form.is_valid():
                    form.save()
                return redirect('orderpage')
        return render(request,'base_clients/create_order.html', context)

def orderpage(request):
    order = Order.objects.all()
    context = {'Order_list':order }
    return render(request, 'base_clients/orders_page.html', context)

def products_page(request):
    
    products = Product.objects.all()
    context = {'Product_list':products }
    return render(request, 'base_clients/products_page.html', context)

def promotions_page(request):
    return render(request,'base_clients/promotions_page.html')

def delete_order(request):
    order = Order.objects.all()
    order.delete()
    return redirect('orderpage')


# def UpdateOrder(request,pk):

#     order = Order.objects.get(id = pk)
#     form = OrderForm(instance=order)

#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request,'base_clients/order_form.html', context)

# def delete_order(request,pk):
#     order = Order.objects.get(id=pk)
#     if request.method == 'POST':
#         order.delete()
#         return redirect('/')

#     context = {'item':order}
#     return render(request,'base_clients/delete.html',context)    