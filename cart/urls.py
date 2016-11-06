from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^$',views.index,name="index"),
    url(r'^cart/$',views.cart,name="cart"),
    # url(r'^cart_handle/$',views.cart_handle,name="cart_handle"),
    # url(r'^cart_change/$',views.cart_change,name="cart_change"),
    # url(r'^register/$',views.register,name="register"),
    # url(r'^place_order/$',views.place_order,name="place_order"),
    url(r'^deleteHander/$',views.deleteHander,name="deleteHander"),
    url(r'^statements/$',views.statements,name="statements"),
 	url(r'^place_order/$',views.place_order,name="place_order"),
    url(r'^place_hander/$',views.place_hander,name="place_hander"),
]
