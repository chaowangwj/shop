from django.shortcuts import *


def login_yz(fn):
    def yz(request):
        if request.session.has_key('uname'):
            r = fn(request)
        else:
            r = redirect('/login/')
        return r
    return yz
