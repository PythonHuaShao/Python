from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(default='',max_length=20)
    uaddress = models.CharField(default='',max_length=100)
    ucode = models.CharField(default='',max_length=6)
    uphone = models.CharField(default='',max_length=12)


# Create your models here.
