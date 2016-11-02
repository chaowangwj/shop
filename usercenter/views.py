# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime
from django.core.urlresolvers import reverse
from . import der

@der.login_yz
def user_center_info(request):
    name = request.session.get('name')
    user = UserInfo.objects.get(uName=name)
    # user = UserInfo.objects.get(uName='wangchao')
    if request.method == 'GET':
        recentsee = user.recentsee_set.all()
        goodlist = []
        for i in recentsee:
            goodlist.append(Goods.objects.get(goodsName=i.goodsName))
        
        return render(request, 'freshFruit/user_center_info.html', {'info': {'user': user, 'recentsee': goodlist[-5:]}})
    elif request.method == 'POST':
        addr = request.POST.get('addr', None)
        phonenumber = request.POST.get('phonenumber', None)
        if addr and phonenumber:
            user.uPhoneNumber = phonenumber
            user.uAddr = addr
            user.save()
        return HttpResponseRedirect(reverse('usercenter:user_center_info'))

@der.login_yz
def user_center_order(request):
    return render(request, 'freshFruit/user_center_order.html')

# @der.login_yz
def user_center_site(request):
    if request.method == 'GET':
        user = UserInfo.objects.get(uName='wangchao')
        addrinfo = user.addrinfo_set.all().filter(isDelete=False)
        list2 = []

        for i in addrinfo:
            a = i.aPhoneNumber[0:]
            list2.append({'id': i.id, 'aProvince': i.aProvince, 'aCity': i.aCity,
                          'aDis': i.aDis, 'aAddressee': i.aAddressee, 'aPhoneNumber': a[0:3] + u'****' + a[7:]})

        return render(request, 'freshFruit/user_center_site.html', {'addrinfo': list2})

    elif request.method == 'POST':
       
        addressee = request.POST.get('addressee', None)
        province = request.POST.get('province', None)
        city = request.POST.get('city', None)
        dis = request.POST.get('dis', None)
        detaaddr = request.POST.get('detaaddr', None)
        postcode = request.POST.get('postcode', None)
        phonenumber = request.POST.get('phonenumber', None)

        if addressee and province and city and detaaddr and str(phonenumber).isdigit() and len(phonenumber) == 11:
            addrinfo = AddrInfo()
            addrinfo.aProvince = AreaInfo.objects.get(id__exact=province)
            addrinfo.aCity = AreaInfo.objects.get(id__exact=city)

            if dis:
                addrinfo.aDis = AreaInfo.objects.get(id__exact=dis)

            addrinfo.aAddressee = addressee
            addrinfo.aDetaAddr = detaaddr
            addrinfo.aPostCode = postcode
            addrinfo.aPhoneNumber = phonenumber
            user = UserInfo.objects.get(uName__exact='wangchao')

            addrinfo.aUser = user
            addrinfo.save()
            print '写入完成'
            # addrinfo.aDefaultAddr =
            return HttpResponseRedirect(reverse('usercenter:user_center_site'))
            # return render(request,'usercenter/user_center_site.html')
        else:
            return HttpResponseRedirect(reverse('usercenter:user_center_site'))
            # return render(request,'usercenter/user_center_site.html')


def areal(request):

    list1 = AreaInfo.objects.filter(aParent__isnull=True)

    list2 = []
    for a in list1:
        list2.append({'id': a.id, 'title': a.aTitle})
    return JsonResponse({'data': list2})


def areal2(request, pid):
    # list1=AreaInfo.objects.filter(aParent_id=pid)
    list1 = AreaInfo.objects.get(pk=pid).areainfo_set.all()
    list2 = []
    for a in list1:
        list2.append({'id': a.id, 'title': a.aTitle})
    return JsonResponse({'data': list2})
