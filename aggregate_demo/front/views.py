from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,BookOrder,Publisher,Author
from django.db.models import Avg,Sum,Count,Max,Min,F,Q
from django.db import connection
def index(request):
    #所有图书定价的平均价格
    #select avg(price) as '平均价格' from book;
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # print(result.query)
    print(connection.queries[-1])
    return HttpResponse('success')

def index2(request):
    #每一本图书销售的平均价格
    result = Book.objects.annotate(avg=Avg("bookorder__price"))
    for res in result:
        print('%s:%s'%(res.name,res.avg))
    # print(result.query)
    print(connection.queries)
    return HttpResponse('success')

def index3(request):
    #总共有多少本书
    # result = Book.objects.aggregate(book_nums=Count("id"))
    # print(result)
    # print(connection.queries)

    #没一本图书的销量
    books = Book.objects.annotate(book_salenums=Count("bookorder__id"))
    for book in  books:
        print('%s:%s' %(book.name,book.book_salenums))
    print(connection.queries)
    return HttpResponse('success')

def index4(request):
    # #作者中最大年龄 和最小年龄
    # result = Author.objects.aggregate(max=Max("age"),min=Min('age'))
    # print(result)
    # print(connection.queries)

    # 每一本图书销售的最大价格 及 最小价格
    books = Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
    for book in  books:
        print('%s:%s:%s' %(book.name,book.max,book.min))
    print(connection.queries)
    return HttpResponse('success')


def index5(request):
    # # 所有图书的销售总额
    # result = BookOrder.objects.aggregate(total=Sum('price'))
    # print(result)
    # print(connection.queries)
    #
    # # 每一本图书的销售总额
    # books = Book.objects.annotate(total=Sum("bookorder__price"))
    # for book in  books:
    #     print('%s:%s' %(book.name,book.total))
    # print(connection.queries)

    # 2020年度所有图书的销售总额
    result = BookOrder.objects.filter(create_time__year=2020).aggregate(total=Sum('price'))
    print(result)
    print(connection.queries)

    # 每一本图书2020年的销售总额
    books = Book.objects.filter(bookorder__create_time__year=2020).annotate(total=Sum("bookorder__price"))
    for book in books:
        print('%s:%s' % (book.name, book.total))
    print(connection.queries)
    return HttpResponse('success')


def index6(request):
    #每一本图书的售价增加10块钱
    # bookorders = BookOrder.objects.all()
    # for bookorder in bookorders:
    #     bookorder.price += 10
    #     bookorder.save()
    # Book.objects.update(price=F('price')+10)
    authors = Author.objects.filter(name=F('email'))
    for author in authors:
        print("%s:%s"%(author.name,author.email))
    print(connection.queries)
    return HttpResponse('success')


def index7(request):
    # books = Book.objects.filter(price__gte=105,rating__gt=4.85)
    # books = Book.objects.filter(Q(price__gte=105)&Q(rating__gt=4.85))
    # books = Book.objects.filter(Q(price__gte=105)|Q(rating__gt=4.85))
    books = Book.objects.filter(Q(price__gte=105)&~Q(name__icontains='传'))
    for book in books:
        print("%s:%s:%s"%(book.name,book.price,book.rating))
    print(connection.queries)
    return HttpResponse('success')