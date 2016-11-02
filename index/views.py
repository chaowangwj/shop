# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
import json

# 首页
def index(request):
	# 拿到产品分类信息
	SortsMsg=GoodSort.objects.all()
	goodMsgList=[]
	goodOtherList=[]
	for sort in SortsMsg:
		goodMsgList.append(sort.goods_set.all().order_by('goodsName')[0:4])
		goodOtherList.append(sort.goods_set.all().order_by('goodsName')[4:7])
	
	name = request.session.get('name',default='')
	user = UserInfo.objects.get(uName=name)
	print goodMsgList
	dic={
		'user':user,
		'sorts':SortsMsg,
		'goodMsgList1':goodMsgList[0],
		'goodMsgList2':goodMsgList[1],
		'goodMsgList3':goodMsgList[2],
		'goodMsgList4':goodMsgList[3],
		'goodMsgList5':goodMsgList[4],
		'goodMsgList6':goodMsgList[5],
		'goodOtherList1':goodOtherList[0],
		'goodOtherList2':goodOtherList[1],
		'goodOtherList3':goodOtherList[2],
		'goodOtherList4':goodOtherList[3],
		'goodOtherList5':goodOtherList[4],
		'goodOtherList6':goodOtherList[5],
		
	}

	return render(request,'freshFruit/index.html',{'info':dic})




def test(request):
	# 拿到产品分类信息
	# SortsMsg=GoodSort.objects.all()
	sort1=GoodSort.objects.filter(id=1)
	# # 拿到分类为新鲜水果的产品的前4条
	# goodMsg=Goods.objects.filter(goodSort_id=1)
	# dic={
	# 	'sorts':SortsMsg,
	# 	'goodsMsg':goodMsg,
	# 	'sortms':sort1
	# }
	# return render(request,'freshFruit/test.html',dic)
	return render(request,'freshFruit/test.html',{'sortms':sort1})
# 关于我们页面
def aboutus(request):
	return render(request,'freshFruit/aboutus.html')
# 联系我们页面
def callus(request):
	return render(request,'freshFruit/callus.html')
# 招聘人才界面
def joinus(request):
	return render(request,'freshFruit/joinus.html')
