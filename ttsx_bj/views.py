#coding=utf-8
from django.shortcuts import render,redirect
from models import UserInfo
from hashlib import sha1
from django.http import JsonResponse
import datetime
import user_decorators
from ttsx_goods.models import GoodsInfo

def register(request):
    context = {'title':'注册','top':'0'}
    return render(request,'ttsx_bj/register.html',context)

def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uemail = post.get('user_email')

    context = {}
    #来源于客户端的验证可能不准确,最好再验证一次
    if len(uname)<5 or len(uname)>20:
        context['error_name'] =  '请输入5-20个字符的用户名'
        return render(request,'ttsx_bj/register.html',context)
        context['uname'] = uname
    else:

        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        user = UserInfo()
        user.uname = uname
        user.upwd = upwd_sha1
        user.uemail = uemail
        user.save()
    return redirect('/user/login/')

def register_valid(request):
    uname = request.GET.get('uname')
    data = UserInfo.objects.filter(uname=uname).count()
    context = {'valid':data}

    return JsonResponse(context)

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'登录','uname':uname,'top':'0'}
    return render(request,'ttsx_bj/login.html',context)

def login_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    ujz = post.get('user_jz',0)

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title':'登录','uname':uname,'upwd':upwd,'top':'0'}
    #如果没有查到数据返回[],如果查到数据返回[UserInfo]
    result = UserInfo.objects.filter(uname=uname)
    if len(result)==0:
        context['error_name'] = '用户名错误'
        return render(request,'ttsx_bj/login.html',context)
    else:
        if result[0].upwd == upwd_sha1:
            #登录成功
            response = redirect(request.session.get('url_path','/'))
            request.session['uid'] = result[0].id
            request.session['uname'] = result[0].uname
            #记住用户名
            if ujz == '1':
                response.set_cookie('uname',uname,expires = datetime.datetime.now()+datetime.timedelta(days = 14))
            else:
                response.set_cookie('uname','',max_age=-1)
            return response
        else:
            #密码错误
            context['error_pwd'] = '密码错误'
            return render(request, 'ttsx_bj/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/user/login/')


def islogin(request):
    result = 0
    if request.session.has_key('uid'):
        result = 1
    return JsonResponse({'islogin':result})


@user_decorators.user_islogin
def user_center_info(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    ids = request.COOKIES.get('goods_ids','').split(',')[:-1]
    goods_list = GoodsInfo.objects.filter(id__in=ids)
    context = {'user':user,'glist':goods_list}
    return render(request,'ttsx_bj/user_center_info.html',context)
@user_decorators.user_islogin
def user_center_order(request):
    context = {}
    return render(request,'ttsx_bj/user_center_order.html',context)
@user_decorators.user_islogin
def user_center_site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])

    if request.method == 'POST':
        post = request.POST
        ushou = post.get('ushou')
        uaddress = post.get('uaddress')
        ucode = post.get('ucode')
        uphone = post.get('uphone')

        user.ushou = ushou
        user.uaddress = uaddress
        user.ucode = ucode
        user.uphone = uphone
        user.save()
    context = {'user':user}
    return render(request,'ttsx_bj/user_center_site.html',context)

# Create your views here.
