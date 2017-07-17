from django.db import models
from ttsx_bj.models import UserInfo
class CartInfo(models.Model):
    goods = models.ForeignKey('ttsx_goods.GoodsInfo')
    user = models.ForeignKey(UserInfo)
    count = models.IntegerField()









# Create your models here.
