#coding=utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import *
from models import *
from django.db.models import *

def index(request):
	return render(request,"freshFruit/index.html")
def register(request):
	return render(request,"freshFruit/register.html")
def place_order(request):
	a = request.POST
	dir = {
		"list":a
	}
	return render(request,"freshFruit/place_order.html",dir)
def cart(request):
	user = UserInfo.objects.get(uName="wangchao")
	cartlist = user.cart_set.all().filter(isDelete=False)
	car_good_list=[]
	for car in cartlist:
		car_good_list.append({'cart':car,'good':Goods.objects.get(id=int(car.goodsName))})

	dic={'lis':car_good_list}
	# print dic
	return render(request,"freshFruit/cart.html",dic)

def deleteHander(request):
	cartId=request.POST.get('cartId',None)
	print cartId
	if cartId:
		cart=Cart.objects.get(id=int(cartId))
		cart.isDelete=True
		cart.save()
		return JsonResponse({'response':'1'})

def statements(request):
	print request.POST
		


	









	# print list1
	# # list1 = Cart.objects.all().filter(isDelete=False)
	# list2 = Goods.objects.all()
	# for a in list1:
	# 	name1 = a.goodsName
	# 	for b in list2:
	# 		name2 = b.goodsName
	# 		if name1==name2:
	# 			b.extra=a.buyCount
	# 			cartlist.append(b)
	# num = 0
	# cart_num = len(cartlist)
	# for c in cartlist:
	# 	num =num+ (c.extra )* (c.goodsPrice)
	# dir = {
	# 	"list3":cartlist,
	# 	"num":num,
	# 	"cart_num":cart_num
	# }
	# return render(request,"freshFruit/cart.html",dir)
def cart_handle(request):
	# a = request.POST.get("goodsName",None)
	a = request.POST.get("goodsName",None)
	b = request.POST.get("username",None)
	user = UserInfo.objects.get(uName=b)
	list1 = user.cart_set.get(goodsName=a)
	# list1 =Cart.objects.get(goodsName=a)
	# print list1
	list1.isDelete=True
	# print list1
	list1.save()
	return jsonResponse({aa:"aa"})
def cart_change(request):
	curr_val = request.POST.get("curr_val",None)
	print curr_val
	a = request.POST.get("goodsName",None)
	print a
	b = request.POST.get("username",None)
	print b
	user = UserInfo.objects.get(uName=b)
	list1 = user.cart_set.get(goodsName=a)
	if list1.buyCount != curr_val:
		list1.buyCount=curr_val
		list1.save()
	return jsonResponse({aa:"aa"})


