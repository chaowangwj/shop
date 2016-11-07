# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime
from usercenter import der
# import os
from django.core.urlresolvers import reverse


@der.login_name
def detail(request,dic):
	goodsId=request.GET.get('goodsId')
	if goodsId:
		good = Goods.objects.get(pk=goodsId)
	newgoodslist=good.goodSort.goods_set.all().order_by("-gPubdate")[0:2]

	GoodsComment=good.goodscomment_set.all().order_by("-commentDate")[0:2]
	if dic['user']:
		flag=False
		rece= dic['user'].recentsee_set.all().order_by('-id')[0:5]
		for i in rece:
			if i.goodsName==goodsId:
				flag=True
		if not flag:
			rec=RecentSee()
			rec.goodsName=goodsId
			rec.user_id=dic['user'].id
			rec.save()
			print '写入rec完成'
	dic2 ={
	'good':good,
	'newgoodslist':newgoodslist,
	'GoodsComment':GoodsComment,
	}
	dic=dict(dic, **dic2)
	return render(request,'freshFruit/detail.html',dic)

@der.login_yz
def comment(request,gid):
	# print request.POST
	comment=request.POST.get('comment',None)
	# goodId=request.POST.get('commgood',None)
	# print comment,goodId
	if comment and gid:
		goodc=GoodsComment()
		goodc.userName=request.session['name']
		goodc.commentDate=datetime.now()
		goodc.comment=comment
		goodc.goods_id=int(gid)
		goodc.save()
		print gid
		# print reverse('detail:detail',kwargs={'goodsId':goodId})reverse('detail:detail',args=[gid])
		return HttpResponseRedirect('/detail/?goodsId='+gid)
@der.login_yz
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




				
			
			

