from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False,default=0)

class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)


class Author(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    desc = models.TextField()
    age = models.IntegerField(null=True,db_column='kangbazi_age',default=18)
    telephone = models.CharField(max_length=11,unique=True)

    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'xiaoliuge'
        ordering = ['-create_time',id]