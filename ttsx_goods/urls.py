from django.conf.urls import url
from . import views
from search_view import MySearchView
urlpatterns = [
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goods_list),
    url(r'^(\d+)/$',views.detail),
    url(r'^search/$',MySearchView.as_view())


]