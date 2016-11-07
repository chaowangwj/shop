# coding=utf-8
from django.shortcuts import render, redirect
from django.http import *
from models import *
from datetime import datetime
import random


def order(request):
	list1 = AddrInfo.objects.filter(isDelete=False).filter(aName='张三').filter(aDefaultAddr=True)
	list2=[]
	for area in list1:
		phone = area.aPhoneNumber[0:3]+'****'+area.aPhoneNumber[7:]
        list2.append({'id': area.id, 'province': area.aProvince,'city':area.aCity,'dis':area.aDis,'addressee':area.aAddressee,'phonenumber':phone,'detail':area.aDetaAddr})
	return render(request, 'freshFruit/place_order.html',{'addr':list2})

def userorder(request):
	#获取页面的位置
	pIndex = request.GET.get('page', None)
	if pIndex == '' or pIndex == None:
		pIndex = '1'
	pIndex=int(pIndex)

	#获得总页面数量
	userlist = Orders.objects.filter(isDelete=False).filter(userOrder=1).order_by("-id")
	listlen = len(userlist)
	i=0
	sumpage=2
	while i < listlen:
		sumpage+=1
		#获得订单中的物品总类数
		orderlist3 = Orders.objects.filter(extra=userlist[i].extra).count()
		print 'orderlist3',orderlist3
		i+=orderlist3
	if sumpage%2 >0:
		sumpage = (sumpage/2) + 1

	else:
		sumpage = sumpage/2
	print 'sumpage',sumpage
	sumpage = list(range(1,sumpage))
	
	#获得页面上第一个应该显示的物品是第几个物品(i)
	i = 0
	for temp in range((pIndex-1)*2):
		orderlist3 = Orders.objects.filter(extra=userlist[i].extra).count()
		i+=orderlist3
	print i
	#构造页面上第一个订单
	list1 = []
	time1 = userlist[i].orderTime
	sumPrice1 = 10
	extra1 = userlist[i].extra
	if userlist[i].isFinish:
		isfinish1 = '已'
		ispay1 = '查物流'
	else:
		isfinish1 = '未'
		ispay1 = '去付款'
	for temp in range(Orders.objects.filter(extra=userlist[i].extra).count()):
		temp = userlist[temp+i]
		sumPrice1+=temp.goodsPrice
		goodPrice = '%.2f'%(temp.goodsPrice/temp.buyCount)
		path = Goods.objects.get(goodsName=temp.goodsName).imgPath
		i+=1
		list1.append({
		 'goodsPrice': temp.goodsPrice,
		 'goodsName':temp.goodsName,
		 'buyCount':temp.buyCount,
		 'orderTime':temp.orderTime,
		 'price':goodPrice,
		 'img':path,
		 })

	#构造页面上的第二个订单
	list2 = []
	time2 = userlist[i].orderTime
	sumPrice2 = 10
	extra2 = userlist[i].extra
	if userlist[i].isFinish:
		isfinish2 = '已'
		ispay2 = '查物流'
	else:
		isfinish2 = '未'
		ispay2 = '去付款'
	for temp in range(Orders.objects.filter(extra=userlist[i].extra).count()):
		temp = userlist[temp+i]
		sumPrice2+=temp.goodsPrice
		goodPrice = '%.2f'%(temp.goodsPrice/temp.buyCount)
		path = Goods.objects.get(goodsName=temp.goodsName).imgPath
		list2.append({
		 'goodsPrice': temp.goodsPrice,
		 'goodsName':temp.goodsName,
		 'buyCount':temp.buyCount,
		 'orderTime':temp.orderTime,
		 'price':goodPrice,
		 'img':path,
		 })

	return render(request, 'freshFruit/user_center_order.html',{
	              'pIndex':pIndex,
	              'sumpage':sumpage,

	              'ispay1':ispay1,
	              'isFinish1':isfinish1,
			      'time1':time1,
			      'ordernumb1':extra1,
			      'list1':list1,
			      'sumPrice1':sumPrice1,

			      'ispay2':ispay2,
	              'isFinish2':isfinish2,
			      'time2':time2,
			      'ordernumb2':extra2,
			      'list2':list2,
			      'sumPrice2':sumPrice2,
			      })
def userinfo(request):
	return render(request, 'freshFruit/user_center_info.html')
def usersite(request):
	return render(request, 'freshFruit/user_center_site.html')
def test(request):

	return render(request, 'freshFruit/user_center_info.html',{'list':list1})



    # goodsName = models.CharField(max_length=30)
    # goodsPrice = models.DecimalField(max_digits=7, decimal_places=2)
    # buyCount = models.IntegerField()
    # isFinish = models.BooleanField(default=False)
    # isDelete = models.BooleanField(default=False)
    # orderTime = models.DateTimeField()
    # extra = models.CharField(max_length=20,null=True,blank=True) #预留
    # userOrder = models.ForeignKey('UserInfo')