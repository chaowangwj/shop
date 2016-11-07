# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from usercenter import der

@der.login_name 
def list(request,dic):
    '''
    商品列表呈现，默认以id排序，可以接收参数按照价格以及购买数量排序，新品推荐取出最新两个种类的商品
    '''
    sort = request.GET.get('sort', None)
    if sort == '' or sort == None:
        sort = 1
    sort = int(sort)
    goodsort = GoodSort.objects.get(id=sort)

    goodslist = goodsort.goods_set.all()

    newgoodslist = goodslist.order_by("-gPubdate")[0:2]  # 新品推荐

    order = request.GET.get('order', None)
    if order == '' or order == None:
        order = 'id'
    if order == 'price':
        orderlist = goodslist.order_by('goodsPrice')  # 排序后的集合
        active = {'price': 'active'}
    elif order == 'id':
        orderlist = goodslist.order_by('id')
        active = {'id': 'active'}
    elif order == 'count':
        orderlist = goodslist.order_by('-saleCount')
        active = {'count': 'active'}
    else:
        return HttpResponse('404')

    pIndex = request.GET.get('page', None)
    orderlist2, plist, pIndex = pagTab(orderlist, pIndex, 5)  # 分页
    if len(plist)>=3:   #页码显示页数
        if len(plist)==pIndex:
            plist=plist[pIndex-3:pIndex]
        elif pIndex==1:
            plist=plist[0:pIndex+2]
        else:
            plist=plist[pIndex-2:pIndex+1]
    SortsMsg=GoodSort.objects.all()
    data = {'goodslist': {
        'newgoodslist': newgoodslist,
        'orderlist': orderlist2,
        'active': active,
        'plist': plist,
        'pIndex': pIndex,
        'ordertype': order,
        'pIndex': pIndex,
        'goodsort': goodsort
    },
    'SortsMsg':SortsMsg
    }
    dic=dict(dic,**data)
    
    return render(request, 'freshFruit/list.html', dic)


def pagTab(list1, pIndex, num):
    '''
    分页函数
    '''
    p = Paginator(list1, num)
    if pIndex == '' or pIndex == None:
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    return list2, plist, pIndex
