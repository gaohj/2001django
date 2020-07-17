from django.shortcuts import render,redirect,reverse
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your models here.
# from .models import People
@login_required(login_url='/login/')
def index(request):
    #创建普通用户
    # user = User.objects.create_user(username='ziwei',email='ziwei@vip.qq.com',password='123456')
    # user.save()
    #创建超级用户
    # user = User.objects.create_superuser(username='huihui',email='huihui@vip.qq.com',password='123456')
    # user.save()
    # user = authenticate(username='huihui',password='123456')
    # if user:
    #     print('登录成功')
    # else:
    #     print('登录失败')
    # user = User.objects.filter(username='huihui').first()
    # user.set_password('666666')
    # user.save()
    # return render(request,'index.html')
#获取黑名单
# def proxy_view(request):
#     blacklist = People.get_blacklist()
#     for black in blacklist:
#         print(black.username)
    return HttpResponse('获取黑名单')

def my_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)
            if user and user.is_active:
                login(request,user)
                if remember:
                    # 设置为None，则表示使用全局的过期时间 14天
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                print(next_url)
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse('登录成功')
            else:
                return HttpResponse('手机号码或者密码错误！')
        else:
            print(form.errors)
            return redirect(reverse('login'))
def my_logout(request):
    logout(request)
    return redirect(reverse('login'))

@login_required(login_url='/login/')
def prifile(request):
    return HttpResponse('这是个人中心')
# def my_authenticate(telephone,password):
#     #根据手机号查询用户是否存在 并拿出详细信息
#     user = User.objects.filter(extension__telephone=telephone).first()
#     if user:
#         is_correct = user.check_password(password)
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None

def one_view(request):
    # user = User.objects.create_user(username='tonglu',email='tonglu@gmail.com',password='123456')
    # user.extension.telephone='13888888888'
    # user.extension.birth = '2001-10-20'
    # user.save()
    # telephone = request.GET.get('telephone')
    # password = request.GET.get('password')
    # user = my_authenticate(telephone,password)
    # if user:
    #     print("验证成功:%s" % user.username)
    # else:
    #     print("验证失败")
    return HttpResponse('一对一模型')


def inherit_view(request):
    user = User.objects.create_user(telephone='13555555555',username='lvtao',email='lvtao@gmail.com',password='123456')
    # user = authenticate(request,username='lvtao',password='123456')
    # if user:
    #     print('验证成功')
    # else:
    #     print('验证失败')
    return HttpResponse('模型继承')


