# coding=utf-8
from haystack.generic_views import SearchView
from models import *
from django.http import *
from django.shortcuts import render

# 重写haystack的视图类，为了在搜索时可以拿到数据，做到搜索页的状态保持
class MySearchView(SearchView):
	def get_context_data(self,*args,**kwargs):
		context = super(MySearchView, self).get_context_data(*args,**kwargs)
		username = self.request.session.get('name', default='')
		number=0
		user=''
		if username:
			user=UserInfo.objects.get(uName=username)
			number=user.cart_set.filter(isDelete=False).count()
			context['user']=user
			context['number']=number
			SortsMsg=GoodSort.objects.all()
			context['SortsMsg']=SortsMsg
		return context







