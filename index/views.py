# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
import json
from usercenter import der
from django.core.urlresolvers import reverse
# 首页
# @der.login_yz
@der.login_name
def index(request,dic):
	# 拿到产品分类信息
	SortsMsg=GoodSort.objects.all()
	message=[]
	for sort in SortsMsg:
		message.append({'sort':sort,'goodMsgList':sort.goods_set.all().order_by('goodsName')[0:4],'goodOtherList':sort.goods_set.all().order_by('goodsName')[4:7]})
		

	dic=dict(dic,**{
		'message':message,
		})
	
	return render(request,'freshFruit/index.html',dic)

def loginOut(request):
	del request.session['name']
	return HttpResponseRedirect(reverse('index:indexPage'))


# 关于我们页面
def aboutus(request):
	return render(request,'freshFruit/aboutus.html')
# 联系我们页面
def callus(request):
	return render(request,'freshFruit/callus.html')
# 招聘人才界面
def joinus(request):
	return render(request,'freshFruit/joinus.html')

def choujiang(request):
	return render(request,'freshFruit/choujiang.html')

