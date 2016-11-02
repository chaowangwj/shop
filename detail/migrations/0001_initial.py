# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddrInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aName', models.CharField(max_length=30)),
                ('aProvince', models.CharField(max_length=15)),
                ('aCity', models.CharField(max_length=15)),
                ('aDis', models.CharField(max_length=15, null=True, blank=True)),
                ('aAddressee', models.CharField(max_length=20)),
                ('aDetaAddr', models.CharField(max_length=30)),
                ('aPostCode', models.CharField(max_length=10, null=True, blank=True)),
                ('aPhoneNumber', models.CharField(max_length=15)),
                ('isDelete', models.BooleanField(default=False)),
                ('aDefaultAddr', models.BooleanField(default=False)),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'addrinfo',
            },
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aTitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, to='detail.AreaInfo', null=True)),
            ],
            options={
                'db_table': 'areainfo',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsName', models.CharField(max_length=30)),
                ('buyCount', models.IntegerField(default=1)),
                ('isDelete', models.BooleanField(default=False)),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsName', models.CharField(max_length=30)),
                ('goodsDesc', models.CharField(max_length=80)),
                ('goodsPrice', models.DecimalField(max_digits=7, decimal_places=2)),
                ('goodsDetail', tinymce.models.HTMLField()),
                ('imgPath', models.ImageField(upload_to=b'uploads/')),
                ('saleCount', models.IntegerField(default=0)),
                ('gPubdate', models.DateTimeField()),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=30)),
                ('commentDate', models.DateTimeField()),
                ('comment', tinymce.models.HTMLField()),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
                ('goods', models.ForeignKey(to='detail.Goods')),
            ],
            options={
                'db_table': 'goodscomment',
            },
        ),
        migrations.CreateModel(
            name='GoodSort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sortName', models.CharField(max_length=10)),
                ('sortPic', models.ImageField(upload_to=b'uploads/')),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'goodsort',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsName', models.CharField(max_length=30)),
                ('goodsPrice', models.DecimalField(max_digits=7, decimal_places=2)),
                ('buyCount', models.IntegerField()),
                ('isFinish', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
                ('orderTime', models.DateTimeField()),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='RecentSee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsName', models.CharField(max_length=30)),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'recentsee',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uName', models.CharField(max_length=30)),
                ('uPassword', models.CharField(max_length=20)),
                ('uEmail', models.CharField(max_length=30)),
                ('uPhoneNumber', models.CharField(max_length=15, null=True)),
                ('uAddr', models.CharField(max_length=50, null=True, blank=True)),
                ('uRegDate', models.DateTimeField()),
                ('isDelete', models.BooleanField(default=False)),
                ('extra', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='recentsee',
            name='user',
            field=models.ForeignKey(to='detail.UserInfo'),
        ),
        migrations.AddField(
            model_name='orders',
            name='userOrder',
            field=models.ForeignKey(to='detail.UserInfo'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goodSort',
            field=models.ForeignKey(to='detail.GoodSort'),
        ),
        migrations.AddField(
            model_name='cart',
            name='userCart',
            field=models.ForeignKey(to='detail.UserInfo'),
        ),
        migrations.AddField(
            model_name='addrinfo',
            name='aUser',
            field=models.ForeignKey(to='detail.UserInfo'),
        ),
    ]
