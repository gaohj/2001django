from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('博凡首页')
    else:
        # return redirect('/login/')
        return redirect(reverse('bofan:login'))

def login(request):
    return HttpResponse('bofan登录首页')
#http://127.0.0.1:8000/?id=111
def detail(request,haha_id):
     bofan_id = request.GET.get('id')
     text = '您输入的id的是:%s' % bofan_id
     return HttpResponse(text)

def book_list_year(request,year):
    text = '您输入的年份是:%s' % year
    return HttpResponse(text)

def book_list_telephone(request,telephone):
    text = '您输入的手机号是:%s' % telephone
    return HttpResponse(text)
