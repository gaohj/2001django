from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.models import Permission,Group,ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required,permission_required

User = get_user_model()
# Create your views here.
def add_permission(request):
    #给article模型添加权限   获取article的content_type_id
    content_type = ContentType.objects.get_for_model(Article)
    # print(content_type)
    Permission.objects.create(codename='for you',name='关于你',content_type=content_type)
    return HttpResponse('添加权限成功')


def operate_permission(request):
    #给用户添加操作文章表的权限  先获取用户 再获取文章表的content_type_id
    user = User.objects.first()
    content_type = ContentType.objects.get_for_model(Article) #获取文章表的权限
    #获取文章表有哪些权限
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        print(permission)
    #将权限给用户加进去
    # user.user_permissions.set(permissions)
    # user.user_permissions.add(permissions[1],permissions[2])
    user.user_permissions.remove(*permissions)
    # user.save()
    # user.user_permissions.clear()
    # if user.has_perm('cms.for you'):
    #     print('拥有这个权限')
    # else:
    #     print('没有这个权限')

    print(user.get_all_permissions())
    return HttpResponse('操作权限成功')


def operate_group(request):
    # group = Group.objects.create(name='学霸')
    # content_type = ContentType.objects.get_for_model(Article)  # 获取文章表的权限
    # permissions = Permission.objects.filter(content_type=content_type)
    # for permission in permissions:
    #     print(permission)
    # group.permissions.set(permissions)
    # group.save()

    group = Group.objects.first()
    user = User.objects.first()
    user.groups.add(group)
    user.save()
    if user.has_perm('cms.for you'):
        print('拥有这个权限')
    else:
        print('没有这个权限')
    return HttpResponse('操作组成功')

#不加 raise_exception=True 如果没有权限一直跳到 登录界面  加上之后 没有权限 报 403 forbidden错误
@permission_required(['cms.add_article','cms.for you'],login_url='/login/',raise_exception=True)
def add_article(request):
    # if request.user.is_authenticated:
    #     print('已经登录了')
    #     if request.user.has_perm('cms.add_article'):
    #         return HttpResponse('这是添加文章的页面，welcome')
    #     else:
    #         return HttpResponse('访问被禁止',status=403)
    # else:
    #     return redirect(reverse('login'))
    return HttpResponse('这是添加文章的页面，welcome')


def index(request):
    return render(request,'index.html')