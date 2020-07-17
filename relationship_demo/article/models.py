from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_name='articles')
    author = models.ForeignKey('frontuser.FrontUser',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '<Article:(id:%s,title:%s)>' % (self.id,self.title)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField('Article',related_name='tags')