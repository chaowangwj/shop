from django.conf.urls import include, url
from . import views
from . import viewsUtils

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regcheck/$',views.regcheck,name='regcheck'),
    url(r'^changekw/$',views.changekw,name='changekw'),
    url(r'^verifycode/$',viewsUtils.verifycode,name='verifycode'),
    url(r'^verify/$',views.verify,name='verify'),
]