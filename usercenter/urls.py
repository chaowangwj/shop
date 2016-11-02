from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^user_center_info/$',views.user_center_info,name='user_center_info'),
    url(r'^user_center_order/$',views.user_center_order,name='user_center_order'),
    url(r'^user_center_site/$',views.user_center_site,name='user_center_site'),
    url(r'^areal/$',views.areal,name='areal'),
    url(r'^areal([0-9]+)/$',views.areal2,name='areal2'),
]