from django.db import models

# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=50)
    b_price = models.FloatField(default=1)


class Game(models.Model):
    g_name = models.CharField(max_length=50)
    g_price = models.FloatField(default=1)

class Movie(models.Model):
    m_name = models.CharField(max_length=50)
    m_price = models.FloatField(default=1)


class User(models.Model):
    u_name = models.CharField(max_length=50)
    u_password = models.CharField(max_length=256)