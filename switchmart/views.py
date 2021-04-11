from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Browse, Filters, Cart
from .forms import PrefForm
from itertools import chain
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View
import statistics
import random

OPTIONS = ((1, 'Food'),(2, 'Books'),(3, 'Mobiles'),(4, 'Laptops'),(5, 'Baby Care'))

def cartToBrowse(l1):
        products=[]
        for product in list(l1):
                prod_name=list(Browse.objects.filter(prod_name=product.prod_name))
                price=list(Browse.objects.filter(price=product.price)) 
                products.append((list(set(prod_name) & set(price)))[0])
        return products

def browse_products(request):
		products=Browse.objects.all().order_by('price')
		print(len(products))
		return render(request, 'switchmart/browse_products.html', {'products':products})

def product_details(request,pk):
        product = get_object_or_404(Browse, pk=pk)
        print("Product.pk",product.pk)
        return render(request, 'switchmart/product_details.html', {'product': product})

def cart_page(request):
        cart_obj=Cart.objects.all().order_by('-date')
        products=cartToBrowse(cart_obj)
        return render(request, 'switchmart/cart_page.html', {'products': products})

def create_cart_obj(request,pk):
		product = get_object_or_404(Browse, pk=pk)
		in_cart=list(Cart.objects.filter(pk=product.pk))
		if(not in_cart):
			Cart.objects.create(pk=product.pk, prod_name=product.prod_name, price=product.price, quantity=1,category=product.category)	
				
		print(product.pk)
		return redirect('cart_page')
#       return render(request, 'switchmart/browse_products.html',{})

def remove(request,pk):
#		del_item=Cart.objects.get(pk=pk)
		del_item=get_object_or_404(Cart, pk=pk)
		del_item.delete()
		return redirect('cart_page')

def recommended(request):
		cart_items = Cart.objects.all()
		categories=[]
		for item in cart_items:
			categories.append(item.category)

		lead_category = statistics.mode(categories)
		recs = list(Browse.objects.filter(category=lead_category))
		recs = random.sample(recs,10)
#		print(recs.pk)
		return render(request, 'switchmart/browse_products.html', {'products' : recs})


		



# Create your views here.
