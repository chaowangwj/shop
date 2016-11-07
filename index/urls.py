# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^/$',views.index,name='indexPage2'),
    url(r'^index/$',views.index,name='indexPage'),
    url(r'^aboutus/$',views.aboutus,name='aboutus'),
    url(r'^callus/$',views.callus,name='callus'),
    url(r'^joinus/$',views.joinus,name='joinus'),
 	url(r'^loginOut/$',views.loginOut,name='loginOut'),
 	url(r'^choujiang/$',views.choujiang,name='choujiang'),

    ]

