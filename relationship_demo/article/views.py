from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category,Tag
from frontuser.models import FrontUser,UserExtension
# Create your views here.

def one_to_many_view(request):
    # frontuser = FrontUser(username='kangbazi')
    # frontuser.save()
    # article = Article(title='草莓长在大棚里边',content='好多人的脖子上也有草莓')
    # article.author = frontuser
    # article.save()

    # user = FrontUser.objects.first() #
    # article = user.article_set.first()#模型名称小写_set
    # print(article)

    # category = Category(name='深度好文')
    # category.save()
    # user = FrontUser.objects.first()
    # article = Article(title='草莓长在大棚里边',content='好多人的脖子上也有草莓')
    # article.author = user
    # article.category = category
    # article.save()

    category = Category.objects.first()
    # print(category.articles.first())
    article = Article(title='先有鸡还是先有蛋',content='这是个问题')
    article.author = FrontUser.objects.first()
    category.articles.add(article,bulk=False)
    # 把文章添加到分类中 需要先把文章保存 否则添加不到分类里
    # 保存文章必须得先保存分类
    #bulk=False 先让你将 文章保存 然后将文章保存到分类中
    return HttpResponse('一对多表关系')

def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school='麻省理工')
    # extension.user = user
    # extension.save()
    # extension = UserExtension.objects.first() #学校是哪个用户的
    # print(extension.user)
    user = FrontUser.objects.first() #用户的学校是什么
    print(user.extension)
    return HttpResponse('一对一表关系')


def many_to_many_view(request):
    # article = Article.objects.get(pk=2)
    # # tag1 = Tag(name='冷门文章')
    # # tag1.save()
    # tag2 = Tag(name='热门文章')
    # tag2.save()
    # # article.tag_set.add(tag1)
    # article.tags.add(tag2)
    article = Article.objects.get(pk=2)
    tags = article.tags.all()
    for tag in tags:
        print(tag)
    return HttpResponse('多对多表关系')