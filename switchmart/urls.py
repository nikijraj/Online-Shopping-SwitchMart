from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#   path('', views.home_page, name='home_page'),
    path('', views.browse_products, name='browse_products'),
	path('product/<int:pk>/', views.product_details, name='product_details'),
#	path('mark_filter/', views.mark_filter, name='mark_filter'),
#	path('search_history/', views.search_history, name='search_history'),
#	path('search_history/<int:pk>/edit', views.edit_search, name='edit_search'),
	#path('make_search/matches.html/', views.get_matches, name='matches'),
#	path('shelving/', views.shelving, name='shelving'),
#   path('shelf_page/',views.shelf_page, name='shelf_page'),
#   path('make_search/shelf_obj/<int:pk>/',views.create_shelf_obj, name='create_shelf_obj'),

#    path('register',views.register,name='register'),
#    path('registered',views.registered,name='registered'),
#    path('/login',views.LoginView.as_view(),name="login"),
#    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#    path('',views.first_page, name='first_page')

]

