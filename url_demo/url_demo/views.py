from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

# http://127.0.0.1:8000/detail/100/1/
def book_detail(request,book_id,book_category):
    text = '您的图书id是:%s,分类是:%s' % (book_id,book_category)
    return HttpResponse(text)

# http://127.0.0.1:8000/login/?next=detail
def login(request):
    next = request.GET.get('next')
    text = '登录完成以后要跳转的url链接是：%s' % next
    return HttpResponse(text)