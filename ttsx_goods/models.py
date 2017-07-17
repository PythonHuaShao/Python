from django.db import models
from tinymce.models import HTMLField
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def _str_(self):
        return self.ttitle.encode('utf-8')
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=30)
    gpic = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    gclick = models.IntegerField()
    gunit = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)
    gkucun = models.IntegerField(default=200)
    gcontext = HTMLField()
    gtype = models.ForeignKey('TypeInfo')


# Create your models here.
