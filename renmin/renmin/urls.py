"""renmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include
# from bofan import views as bofan_view
# from shaozhe import views as shaozhe_view
def index(request):
    return HttpResponse('仁敏兄')
#httt://127.0.0.1:8000/renmin/
#httt://127.0.0.1:8000/huihui/
urlpatterns = [
    # path('',index),
    path('',include('bofan.urls')),
    #两个实例
    #http://127.0.0.1:9000/shaozhe1
    #http://127.0.0.1:9000/shaozhe1/login/
    #http://127.0.0.1:9000/shaozhe2
    #http://127.0.0.1:9000/shaozhe2/login/
    path('shaozhe1/',include('shaozhe.urls',namespace='shaozhe1')),
    path('shaozhe2/',include('shaozhe.urls',namespace='shaozhe2')),
    # path('bofan/',bofan_view.index),
    # path('bofan/detail/',bofan_view.detail),
    # path('shaozhe/',saozhe_view.index),
    # path('shaozhe/detail/<shaozhe_id>/',shaozhe_view.detail),

    #同一个后台 不同的地址登录
    # a团队 没有登录 a团队登录页
    # b团队 没有登录 b团队登录页



]
