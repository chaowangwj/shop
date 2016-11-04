# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime
from usercenter import der
import os


@der.login_name
def detail(request,dic):
	goodsId=request.GET.get('goodsId',None)
	if goodsId:
		good = Goods.objects.get(pk=goodsId)
	newgoodslist=good.goodSort.goods_set.all().order_by("-gPubdate")[0:2]
	# name=request.session.get('name')
	# user=UserInfo.objects.get(uName=name)
	# number=user.cart_set.filter(isDelete=False).count()
	# print newgoodslist
	# dic['good']=good
	# dic['newgoodslist']=newgoodslist
	dic2 ={
	'good':good,
	'newgoodslist':newgoodslist
	}
	dic=dict(dic, **dic2)
	

	return render(request,'freshFruit/detail.html',dic)


def addcart(request):
	goodsID=request.POST.get('goodsName',None)
	buyCount=request.POST.get('buyCount',None)
	if goodsID and buyCount:
		name=request.session['name']
		user=UserInfo.objects.get(uName=name)
		cart=Cart()
		cart.goodsName=goodsID  #goodsName存储商品id 字符串类型，待修改
		cart.buyCount=int(buyCount)
		cart.userCart_id=user.pk
		cart.save()
		number=user.cart_set.filter(isDelete=False).count()
		print '加入成功'
		return JsonResponse({'number':number})




				
			
			

