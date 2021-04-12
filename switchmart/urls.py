from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.browse_products, name='browse_products'),
	path('product/<int:pk>/', views.product_details, name='product_details'),
	path('cart_page/',views.cart_page, name='cart_page'),
	path('prod_added/<int:pk>/',views.create_cart_obj, name='create_cart_obj'),
	path('qty_up/<int:pk>/',views.qty_up, name='qty_up'),
	path('qty_down/<int:pk>/',views.qty_down, name='qty_down'),
	path('remove/<int:pk>/', views.remove, name='remove'),
	path('recommended/', views.recommended, name='recommended'),
]

