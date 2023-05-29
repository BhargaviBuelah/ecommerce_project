from django.urls import path
from todoapp import views
urlpatterns = [
    path('home',views.index),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('index',views.home),
    path('product',views.product),
    path('contact',views.contact),
    path('username/<username>',views.uname),
    path('pdashboard',views.dash_product),
    #path('elec',views.filter_electronics),
    #path('groc',views.filter_grocery),
    #path('cloths',views.filter_cloths),
    path('filter/<vcat>',views.filter),
    path('pfilter/<p>',views.pfilter),
    path('sort/<sv>',views.sort),
    path('prange',views.prange),
    path('formapi',views.empform),
    path('modelform',views.productform),
    path('register',views.register),
    path('login',views.user_login),
    path('setcookie',views.setcookie),
    path('getcookie',views.getcookie),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('logout',views.user_logout),


]
