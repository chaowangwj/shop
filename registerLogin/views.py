# coding=utf-8
# from django.shortcuts import render
# from django.http import *
# from models import *
# from datetime import datetime


# # Create your views here.
# def index(request):
	
# 	return render(request, 'freshFruit/index.html')


# def register(request):
# 	if request.method == 'GET':
# 		return render(request, 'freshFruit/register.html')
# 	elif request.method == 'POST':
# 		user_name = request.POST.get('user_name', None)
# 		password = request.POST.get('pwd', None)
# 		email = request.POST.get('email', None)
# 		if user_name and password and email:
# 			try:
# 				if UserInfo.objects.get(uName=user_name):
# 					pass
# 			except Exception, e:
# 				user = UserInfo()
# 				user.uName = user_name
# 				user.uPassword = password
# 				user.uEmail = email
# 				user.uRegDate = datetime.now()
# 				user.save()
# 				print '写入完成'
# 				return HttpResponseRedirect('/login/')
# 			else:
# 				print 'user has exis:不允许注册'
# 				return render(request, 'freshFruit/register.html')
# 			finally:
# 				pass


# def regcheck(request):
# 	name = request.GET.get('name', None)
# 	if name:
# 		try:
# 			if UserInfo.objects.get(uName=name):
# 				pass
# 		except Exception, e:
# 			print 'exception:注册用户不存在可以注册'
# 			return JsonResponse({'find': 'False'})
# 		else:
# 			print 'user has exis:不允许注册'
# 			return JsonResponse({'find': 'True'})
# 		finally:
# 			pass
# 	else:
# 		return HttpResponse('未接受到数据')


# def login(request):
# 	if request.method == 'GET':
# 		return render(request, 'freshFruit/login.html')
# 	elif request.method == 'POST':
# 		name=request.POST.get('username',None)
# 		password=request.POST.get('pwd',None)
# 		if name and password:
# 			try:
# 				user = UserInfo.objects.get(uName=name)
# 				if user.uPassword==password:
# 					if request.POST.get('check', None) == 'on':
# 						request.session['name'] = name     #状态保持	
# 					return HttpResponseRedirect('/index/') 
# 				else:
# 					return render(request, 'freshFruit/login.html',{'error':{'password':'密码输入有误，请重新输入'}})
# 			except Exception, e:
# 				return render(request, 'freshFruit/login.html',{'error':{'name':'用户名不存在，请重新输入'}})
# 			else:
# 				pass
# 		else:
# 			return render(request, 'freshFruit/login.html',{'error':{'name':'请输入用户名','password':'请输入密码'}})
# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime
from usercenter import der

def index(request):
	return render(request, 'freshFruit/index.html')

def register(request):
	if request.method == 'GET':
		return render(request, 'freshFruit/register.html')
	elif request.method == 'POST':
		user_name = request.POST.get('user_name', None)
		password = request.POST.get('pwd', None)
		email = request.POST.get('email', None)
		if user_name and password and email:
			try:
				if UserInfo.objects.get(uName=user_name):
					pass
			except Exception, e:
				user = UserInfo()
				user.uName = user_name
				user.uPassword = password
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
		if name and password:
			try:
				user = UserInfo.objects.get(uName=name)
				if user.uPassword==password:
					if request.POST.get('check', None) == 'on':
						request.session['name'] = name   
						# request.session['password'] = password    #状态保持
					else:	
						request.session['name'] = name
						request.session.set_expiry(10)    #超时测试
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
		if user_name and password and email:
			auser = UserInfo.objects.get(uName=user_name)
			if auser.uEmail == email:
				auser.uPassword = password
				auser.save()
				return HttpResponseRedirect('/login/')
			else:
				return render(request, 'freshFruit/changekw.html',{'error':{'email':'邮箱错误，请重新输入'}})

	return render(request, 'freshFruit/changekw.html')
