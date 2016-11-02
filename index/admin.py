# coding=utf-8
from django.contrib import admin
from . models import *

class GoodSortAdmin(admin.ModelAdmin):
	list_dispaly=['sortName','sortPic']
class GoodsAdmin(admin.ModelAdmin):
	list_dispaly=['goodsName','goodsDesc','goodsPrice','goodsDetail','imgPath','saleCount','gPubdate']
admin.site.register(GoodSort,GoodSortAdmin)
admin.site.register(Goods,GoodsAdmin)
