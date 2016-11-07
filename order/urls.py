from django.conf.urls import include, url
from . import views

urlpatterns = [
   
    url(r'^place_order.html/$',views.order,name='place_order'),
    url(r'^index.html/$',views.index,name='index'),
    url(r'^user_center_order.html/$',views.userorder,name='user_center_order'),
    url(r'^user_center_info.html/$',views.userinfo,name='user_center_info'),
    url(r'^user_center_site.html/$',views.usersite,name='user_center_site'),
    url(r'^test/$',views.test,),
    ]