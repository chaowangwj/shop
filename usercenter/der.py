from django.shortcuts import *
from models import *

def login_name(fn):
    def fun(request, *args):
        username = request.session.get('name', default='')
        number=0
        user=''
        print username
        if username:
			user=UserInfo.objects.get(uName=username)
			number=user.cart_set.filter(isDelete=False).count()
        dic = {
            'user': user,
            'number':number,

        }
        result = fn(request, dic, *args)
        return result
    return fun


def login_yz(fn):
    def fun(request, *args):
        if request.session.has_key('name'):
            result = fn(request, *args)
        else:
            result = redirect('/login/')
        return result
    return fun