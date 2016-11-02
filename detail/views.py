# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime



def detail(request):

	goodsId=request.GET.get('goodsId',None)
	if goodsId:
		good = Goods.objects.get(pk=goodsId)
	
	newgoodslist=good.goodSort.goods_set.all().order_by("-gPubdate")[0:2]
	print newgoodslist
	dic ={
	'good':good,
	'newgoodslist':newgoodslist
	}

	return render(request,'freshFruit/detail.html',dic)




				
			
			

