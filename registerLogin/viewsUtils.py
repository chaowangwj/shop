# coding=utf-8
from django.http import *
# 引入绘图模块
from PIL import Image, ImageDraw, ImageFont
import random
import cStringIO

def verifycode(request):
	# 定义一个变量用于画布打背景色和宽高
	bgcolor = (random.randrange(20, 100), random.randrange(
		20, 100), 255)
	width = 100
	height = 33
	# 创建画布对象
	im=Image.new('RGB',(width,height),bgcolor)
	# 创建画笔对象
	draw=ImageDraw.Draw(im)
	# 调用画笔打point()函数绘制噪点
	for i in range(0,100):
		xy=(random.randrange(0,width),random.randrange(0,height))
		fill=(random.randrange(0,255),255,random.randrange(0,255))
		draw.point(xy,fill=fill)
	# 定义产生验证码的素材字符
	str1='ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
	# 随机选择４个值作为验证码
	rand_str=''
	for i in range(0,4):
		rand_str+=str1[random.randrange(0,len(str1))]
	# 构造字体对象
	font=ImageFont.truetype('FreeMono.ttf',27)
	# 构造字体颜色
	fontcolor=(255,random.randrange(0,255),random.randrange(0,255))
	# 绘制4个字[第一个参数表示距离左边的位置]
	draw.text((5,2),rand_str[0],font=font,fill=fontcolor)
	draw.text((25,2),rand_str[1],font=font,fill=fontcolor)
	draw.text((50,2),rand_str[2],font=font,fill=fontcolor)
	draw.text((75,2),rand_str[3],font=font,fill=fontcolor)
	# 释放画笔
	del draw
	# 存入session用于做进一步验证
	request.session['verifycode']=rand_str
	# 内存文件操作
	buf=cStringIO
	buf=cStringIO.StringIO()
	# 将图片保存在内存中，文件类型为png
	im.save(buf,'png')
	# 将内存中的图片数据返回给客户端，ＭＩＭＥ类型为图片png
	return HttpResponse(buf.getvalue(),'image/png')