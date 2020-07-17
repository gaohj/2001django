from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse
from django.utils.timezone import make_aware
# Create your views here.
def index(request):

    category = Category(name='传奇故事')
    category.save()
    article = Article(title='钢铁是怎么炼成的',content='铁棒磨成针的故事')
    article.category = category
    article.save()
    return HttpResponse('ok')

def index1(request):
    # article = Article.objects.get(pk=1)
    article =  Article.objects.filter(title__iexact="钢铁是怎么炼成的")
    print(article.query)
    return HttpResponse('index1')

def index2(request):
    # article = Article.objects.get(pk=1)
    article =  Article.objects.filter(title__icontains='钢铁')
    print(article.query)
    return HttpResponse('index2')

def index3(request):
    #查找文章id为 1 2 3 的分类

    articles = Article.objects.filter(id__in=[1,2,3])
    for article in articles:
        print(article)

    categories = Category.objects.filter(articles__in=[1,2,3])
    for categorie in categories:
        print(categorie)
    return HttpResponse('index3')

from datetime import datetime,time
def index4(request):
    # start_time = make_aware(datetime(year=2020,month=7,day=11,hour=16,minute=0,second=0))
    # end_time = make_aware(datetime(year=2020,month=7,day=15,hour=20,minute=0,second=0))
    # articles = Article.objects.filter(create_time__range=(start_time,end_time))
    # print(articles.query)
    # for article in articles:
    #     print(article)
    # articles = Article.objects.filter(create_time__year__gte=2020)
    start_time = time(hour=6,minute=10,second=20)
    end_time = time(hour=23,minute=20,second=30)
    articles = Article.objects.filter(create_time__time__range=(start_time,end_time))
    print(articles.query)
    for article in articles:
        print(article)
    return HttpResponse('index4')


def index5(request):
    articles = Article.objects.filter(title__iregex=r"^钢")
    print(articles.query)
    print(articles)
    return HttpResponse('index5')

#标题中包含 钢铁的文章的分类
def index6(request): #articles 模型中 related_name  或者 releated_query_name
    categories = Category.objects.filter(articles__title__contains='钢铁')
    print(categories.query)
    # for category in categories:
    #     print(category)
    return HttpResponse('index6')