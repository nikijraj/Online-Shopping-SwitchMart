from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Browse, Filters, Cart
#from .forms import PrefForm
from itertools import chain
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View

OPTIONS = ((1, 'Food'),(2, 'Books'),(3, 'Mobiles'),(4, 'Laptops'),(5, 'Baby Care'))


def browse_products(request):
	products=Browse.objects.all().order_by('price')
	return render(request, 'switchmart/browse_products.html', {'products':products})

def product_details(request,pk):
    product = get_object_or_404(Browse, pk=pk)
    return render(request, 'switchmart/product_details.html', {'product': product})


# Create your views here.
