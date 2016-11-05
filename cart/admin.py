from django.contrib import admin
from models import *

class GoodsAdmin(admin.ModelAdmin):
	list_display = ["id","goodsName","goodsPrice","imgPath"]
class CartAdmin(admin.ModelAdmin):
	list_display = ["id","goodsName","buyCount","isDelete","userCart"]

admin.site.register(UserInfo)
admin.site.register(AreaInfo)
admin.site.register(AddrInfo)
admin.site.register(GoodSort)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(GoodsComment)
admin.site.register(Cart,CartAdmin)
admin.site.register(Orders)
admin.site.register(RecentSee)


