from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^list/$', views.list, name='list'),
  
]
 # url(r'^list/$',views.list,name='list'),