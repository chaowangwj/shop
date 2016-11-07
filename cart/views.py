#coding=utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import *
from models import *
from django.db.models import *
from datetime import datetime
# from django.utils import timezone
import time
from usercenter import der
@der.login_yz
@der.login_name
def cart(request,dic):
	# user = UserInfo.objects.get(uName="wangchao")
	cartlist = dic['user'].cart_set.all().filter(isDelete=False)
	car_good_list=[]
	for car in cartlist:
		car_good_list.append({'cart':car,'good':Goods.objects.get(id=int(car.goodsName))})
	dic=dict(dic,**{'lis':car_good_list})

	return render(request,"freshFruit/cart.html",dic)

@der.login_yz
def deleteHander(request):
	cartId=request.POST.get('cartId',None)
	print cartId
	if cartId:
		cart=Cart.objects.get(id=int(cartId))
		cart.isDelete=True
		cart.save()
		return JsonResponse({'response':'1'})
		

def statements(request):
	count=request.POST.getlist('count',None)
	goodId=request.POST.getlist('id',None)
	print count
	print '......'
	print goodId

@der.login_yz
@der.login_name		
def place_order(request,dic):
	# user=UserInfo.objects.get(uName="wangchao")
	cartId=[]
	if request.method == 'GET':
		count=request.GET.get('count',None)
		goodId=request.GET.get('id',None)
		goodId=[goodId]
	elif request.method == 'POST':
		count=request.POST.getlist('count',None)
		cartId=request.POST.getlist('id',None)
		goodId=[]
		j=0
		for i in cartId:
			cart=Cart.objects.get(id=int(i))
			goodId.append(cart.goodsName)
			if int(count[j]) != cart.buyCount:
				cart.buyCount=int(count[j])
				cart.save()
			j += 1
	else:
		pass

	orderlist=[]
	freight = 10
	sumprice=0
	for i in range(len(goodId)):
		# if int(count[i]) != Cart.objects.filter
		goods = Goods.objects.get(id=int(goodId[i]))
		orderdic={'goods':goods,'count':i+1,'sumtotal':goods.goodsPrice*int(count[i]),'goodscount':count[i]}
		if len(cartId)>0:
			orderdic['cartId']=cartId[i]
		orderlist.append(orderdic)
		sumprice += goods.goodsPrice*int(count[i])
	# area = AddrInfo.objects.filter(aUser_id=user.id).get(aDefaultAddr=True)
	AddrList=dic['user'].addrinfo_set.all()
	# print AddrList
	dic=dict(dic,**{
		'AddrList':AddrList,
		'orderlist':orderlist,
		'allprice':sumprice+freight,
		'freight':freight,
		'goodsamount':len(goodId),
		'alltotal': sumprice,
		'cartId':cartId,
	})
	return render(request,"freshFruit/place_order.html",dic)

@der.login_yz
@der.login_name
def place_hander(request,dic):
	# user=UserInfo.objects.get(uName="wangchao")
	addr= request.POST.get('addr')
	goodscount=request.POST.get('goodscount')
	goodsId= request.POST.get('goodsId')  #如果是立即购买的获取物品id
	cartIdList= request.POST.getlist('cartId') #如果是购物车结算的的获取购物车id

	print cartIdList
	orders=Orders()
	orders.orderTime=datetime.now()
	orders.orderNumber=str(int(time.time()))
	orders.userOrder_id=dic['user'].id
	orders.save()
	if cartIdList[0]:
		for i in cartIdList:
			cart=Cart.objects.get(id=int(i))
			goods=Goods.objects.get(id=int(cart.goodsName))
			OrderDetail=orders.orderdetail_set.create(goodsName=goods.goodsName,goodsPrice=goods.goodsPrice,buyCount=cart.buyCount,good_id_id=goods.id)
			OrderDetail.save()
			cart.isDelete=True
			cart.save()
	else:
		goods=Goods.objects.get(id=int(goodsId))
		orders.orderdetail_set.create(goodsName=goods.goodsName,goodsPrice=goods.goodsPrice,buyCount=int(goodscount),good_id_id=goods.id)
	return HttpResponseRedirect(reverse('usercenter:user_center_order'))

			

