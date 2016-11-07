
# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime
from usercenter import der
import hashlib

# 验证码测试页
def verify(request):
	return render(request,'freshFruit/verify.html')

def index(request):
	return render(request, 'freshFruit/index.html')

def register(request):
	if request.method == 'GET':
		return render(request, 'freshFruit/register.html')
	elif request.method == 'POST':
		user_name = request.POST.get('user_name', None)
		password = request.POST.get('pwd', None)
		email = request.POST.get('email', None)
		if user_name and len(password)>=8 and email:
			try:
				if UserInfo.objects.get(uName=user_name):
					pass
			except Exception, e:
				user = UserInfo()
				user.uName = user_name
				n=hashlib.md5()
				n.update(password)
				user.uPassword = n.hexdigest()
				user.uEmail = email
				user.uRegDate = datetime.now()
				user.save()
				print '写入完成'
				return HttpResponseRedirect('/login/')
			else:
				print 'user has exis:不允许注册'
				return render(request, 'freshFruit/register.html')
			finally:
				pass


def regcheck(request):
	name = request.GET.get('name', None)
	if name:
		try:
			if UserInfo.objects.get(uName=name):
				pass
		except Exception, e:
			print 'exception:注册用户不存在可以注册'
			return JsonResponse({'find': 'False'})
		else:
			print 'user has exis:不允许注册'
			return JsonResponse({'find': 'True'})
		finally:
			pass
	else:
		return HttpResponse('未接受到数据')

@der.login_name
def login(request,dic):
	if request.method == 'GET':
		return render(request, 'freshFruit/login.html',dic)
	elif request.method == 'POST':
		name=request.POST.get('username',None)
		password=request.POST.get('pwd',None)
		vecode=request.POST.get('ucode')
		#先验证验证码防止暴力破解
		if vecode.upper()!=request.session['verifycode']:
			return render(request, 'freshFruit/login.html',{'error':{'password':'验证码错误'}})
		if name and password:
			try:
				user = UserInfo.objects.get(uName=name)
				# 如果用户密码和验证都正确，登陆成功
				n=hashlib.md5()
				n.update(password)
				if user.uPassword==n.hexdigest():
					if request.POST.get('check', None) == 'on':
						request.session['name'] = name   
						# request.session['password'] = password    #状态保持
					else:	
						request.session['name'] = name
						request.session.set_expiry(0)    #超时测试
					return HttpResponseRedirect('/index/') 
				else:
					return render(request, 'freshFruit/login.html',{'error':{'password':'密码输入有误，请重新输入'}})
			except Exception, e:
				return render(request, 'freshFruit/login.html',{'error':{'name':'用户名不存在，请重新输入'}})
			else:
				pass
		else:
			return render(request, 'freshFruit/login.html',{'error':{'name':'请输入用户名','password':'请输入密码'}})

# 密码修改
def changekw(request):
	if request.method == 'GET':
		return render(request, 'freshFruit/changekw.html')
	elif request.method == 'POST':
		user_name = request.POST.get('user_name', None)
		password = request.POST.get('pwd', None)
		email = request.POST.get('email', None)
		if user_name and len(password)>=8 and email:
			auser = UserInfo.objects.get(uName=user_name)
			if auser.uEmail == email:
				n=hashlib.md5()
				n.update(password)
				auser.uPassword = n.hexdigest()
				auser.save()
				return HttpResponseRedirect('/login/')
			else:
				return render(request, 'freshFruit/changekw.html',{'error':{'email':'邮箱错误，请重新输入'}})

	return render(request, 'freshFruit/changekw.html')
