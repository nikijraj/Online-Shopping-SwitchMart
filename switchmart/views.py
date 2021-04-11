from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Browse, Filters, Cart
from .forms import PrefForm
from itertools import chain
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View

OPTIONS = ((1, 'Food'),(2, 'Books'),(3, 'Mobiles'),(4, 'Laptops'),(5, 'Baby Care'))

def cartToBrowse(l1):
        products=[]
        for product in list(l1):
                prod_name=list(Browse.objects.filter(prod_name=product.prod_name))
                price=list(Browse.objects.filter(price=product.price)) 
                products.append((list(set(prod_name) & set(price)))[0])
        print(products)
        return products

def browse_products(request):
	products=Browse.objects.all().order_by('price')
	print(len(products))
	return render(request, 'switchmart/browse_products.html', {'products':products})

def product_details(request,pk):
    product = get_object_or_404(Browse, pk=pk)
    return render(request, 'switchmart/product_details.html', {'product': product})

def cart_page(request):
        cart_obj=Cart.objects.all().order_by('-date')
        products=cartToBrowse(cart_obj)
        return render(request, 'switchmart/cart_page.html', {'products': products})

def create_cart_obj(request,pk):
        product = get_object_or_404(Browse, pk=pk)
        print(product)
        Cart.objects.create(prod_name=product.prod_name, price=product.price, quantity=1)
        return redirect('cart_page')


# Create your views here.
