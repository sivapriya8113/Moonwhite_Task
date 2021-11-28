from django.urls import path

from . import views

urlpatterns=[
    #path('',views.api_overview, name='api_overview'),
    path('insert-customer/', views.InsertCustomer, name='insert-customer'),
    path('product-list/', views.showall, name='product-list'),


]








