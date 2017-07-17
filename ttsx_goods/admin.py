from django.contrib import admin
from models import *
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
admin.site.register(TypeInfo,TypeAdmin)
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle','gprice']
    list_per_page = 15

admin.site.register(GoodsInfo,GoodsAdmin)