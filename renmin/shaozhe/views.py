from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('少喆首页')
    else:
        # return redirect('/login/')
        #获取当前的实例
        current_namespace = request.resolver_match.namespace
        print(current_namespace)
        # return redirect(reverse('shaozhe:login'))
        return redirect(reverse('%s:login'%current_namespace))

def login(request):
    return HttpResponse('shaozhe登录首页')
#http://127.0.0.1:8000/?id=111
def detail(request,shaozhe_id):
     text = '您输入的id的是:%s' % shaozhe_id
     return HttpResponse(text)
