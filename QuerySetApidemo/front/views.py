from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,BookOrder,Publisher,Author
from django.db.models import F,Q,Count,Prefetch
from django.db import connection
from django.contrib.auth.models import User
def index(request):
    # books = Book.objects.filter(id__gte=1).exclude(id=4)
    # print(books.query)
    # for book in books:
    #     print(book)
    books = Book.objects.annotate(author_name=F("author__name"))
    for book in books:
        print("%s:%s" % (book.name,book.author_name))
    print(connection.queries)
    return HttpResponse('index')


def index2(request):
    orders = BookOrder.objects.all()
    # orders = BookOrder.objects.order_by('-create_time','-price')
    for order in orders:
        print("%s:%s:%s" % (order.id,order.create_time,order.price))
    print(connection.queries)
    return HttpResponse('index2')

def index3(request):
    #根据每一本书的销量做一下排序
    books = Book.objects.annotate(order_num=Count("bookorder__id")).order_by('-order_num')
    for book in books:
        print("%s:%s" %(book.name,book.order_num))
    return HttpResponse('index3')

def index4(request):
    # books = Book.objects.values('id','name',author_name=F("author__name"))
    books = Book.objects.values_list('name',flat=True)
    print(type(books))
    for book in books:
        print(book)
    return HttpResponse('index4')

def index5(request):
    # books = Book.objects.all()
    # books = Book.objects.select_related("author","publisher")
    # # print(type(books))
    # for book in books:
    #     print(book.author.name)
    #     print(book.publisher.name)
    #
    # context = {
    #     'books':books
    # }
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    # context = {
    #     'books':books
    # }
    # books = Book.objects.prefetch_related('author')
    # for book in books:
    #     print(book.author)
    #查询图书销售价格大于90的图书
    prefetch = Prefetch("bookorder_set",queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)
    context = {
        'books':books
    }
    return render(request,'index5.html',context=context)


def index6(request):
    # books = Book.objects.defer('name')
    books = Book.objects.only('rating')
    for book in books:
        print("%s" %(book.name)) #如果你在查询的时候排除掉name字段  也不打印name
        #这个时候sql语句就不会查询name
        #及时defer制订了name 排除  但是 你打印book.name
        #这时候 sql语句也会去查name
    print(connection.queries)
    return HttpResponse('index6')


def index7(request):
    # books = Publisher.objects.get_or_create(name="仁敏出版社")
    # books = Publisher.objects.bulk_create([
    #     Publisher(name='大根出版社'),
    #     Publisher(name='同露出版社'),
    #     Publisher(name='子威出版社'),
    # ])
    # book = Book.objects.filter(name='三国演义').exists()
    # if book:
    #     print('存在')

    # books = Book.objects.filter(bookorder__price__gte=90).order_by('bookorder__price').distinct()
    # for book in books:
    #     print(book)
    # print(connection.queries)
    # bookorder = BookOrder.objects.update(price=F('price')-5)
    # bookorders = BookOrder.objects.all()
    # for bookorder in bookorders:
    #     bookorder.price = bookorder.price+5
    #     bookorder.save()

    # publisher = Publisher.objects.filter(id__gt=2).delete()

    books = Book.objects.all()[1:2] #从1 截取到2  包含2 不包含1
    for book in  books:
        print(book)
    return HttpResponse('index7')
