from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        permissions = [
            # permission表中的 code_name  name
            ('view_article','看文章的权限'),
            ('black_article','拉黑文章的权限'),
        ]
