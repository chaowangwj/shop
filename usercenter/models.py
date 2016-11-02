# coding=utf-8
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


# 用户表

class UserInfo(models.Model):
    uName = models.CharField(max_length=30)
    uPassword = models.CharField(max_length=20)
    uEmail = models.CharField(max_length=30)
    uPhoneNumber = models.CharField(max_length=15, null=True)
    uAddr = models.CharField(max_length=50, null=True, blank=True)
    uRegDate = models.DateTimeField()
    isDelete = models.BooleanField(default=False)
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'userinfo'

    def __str__(self):
        return self.uName.encode('utf-8')

# 省市区表


class AreaInfo(models.Model):
    aTitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

    class Meta():
        db_table = 'areainfo'

    def __str__(self):
        return self.aTitle.encode('utf-8')

# 地址信息表


class AddrInfo(models.Model):
    # aName = models.CharField(max_length=30) #账户名
    aProvince = models.CharField(max_length=15)
    aCity = models.CharField(max_length=15)
    aDis = models.CharField(max_length=15, null=True, blank=True)
    aAddressee = models.CharField(max_length=20)  # 收信人
    aDetaAddr = models.CharField(max_length=30)
    aPostCode = models.CharField(max_length=10, null=True, blank=True)
    aPhoneNumber = models.CharField(max_length=15)
    isDelete = models.BooleanField(default=False)
    aDefaultAddr = models.BooleanField(default=False)  # 默认地址
    extra = models.CharField(max_length=20,null=True,blank=True) #预留
    aUser = models.ForeignKey('UserInfo')

    class Meta():
        db_table = 'addrinfo'

    def __str__(self):
        return self.aPhoneNumber.encode('utf-8')

# 商品种类表


class GoodSort(models.Model):
    sortName = models.CharField(max_length=10)
    sortPic = models.ImageField(upload_to='uploads/')
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'goodsort'

    def __str__(self):
        return self.sortName.encode('utf-8')

# 商品表


class Goods(models.Model):
    goodsName = models.CharField(max_length=30)
    goodsDesc = models.CharField(max_length=80)
    goodsPrice = models.DecimalField(max_digits=7, decimal_places=2)
    goodsDetail = HTMLField()
    imgPath = models.ImageField(upload_to='uploads/')
    saleCount = models.IntegerField(default=0)
    goodSort = models.ForeignKey('GoodSort')
    gPubdate=models.DateTimeField()
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'goods'

    def __str__(self):
        return self.goodsName.encode('utf-8')

# 商品评论


class GoodsComment(models.Model):
    userName = models.CharField(max_length=30)
    commentDate = models.DateTimeField()
    comment = HTMLField()
    goods = models.ForeignKey('Goods')
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'goodscomment'

    def __str__(self):
        return self.userName.encode('utf-8')

# 购物车表


class Cart(models.Model):
    goodsName = models.CharField(max_length=30)
    buyCount = models.IntegerField(default=1)
    isDelete = models.BooleanField(default=False)
    userCart = models.ForeignKey('UserInfo')
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'cart'

    def __str__(self):
        return self.goodsName.encode('utf-8')

# 订单表


class Orders(models.Model):
    goodsName = models.CharField(max_length=30)
    goodsPrice = models.DecimalField(max_digits=7, decimal_places=2)
    buyCount = models.IntegerField()
    isFinish = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    orderTime = models.DateTimeField()
    extra = models.CharField(max_length=20,null=True,blank=True) #预留
    userOrder = models.ForeignKey('UserInfo')

    class Meta():
        db_table = 'orders'

    def __str__(self):
        return self.goodsName.encode('utf-8')

#最近浏览
class RecentSee(models.Model):
    goodsName=models.CharField(max_length=30)
    extra = models.CharField(max_length=20,null=True,blank=True) #预留
    user=models.ForeignKey('UserInfo')
    class Meta():
        db_table='recentsee'
    def __str__(self):
        return self.goodsName.encode('utf-8')

  

