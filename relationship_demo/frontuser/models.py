from django.db import models

# Create your models here.
class FrontUser(models.Model):
    username = models.CharField(max_length=100,unique=True,null=False)

    def __str__(self):
        return '<FrontUser:(id:%s,username:%s)>' % (self.id,self.username)


class UserExtension(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("FrontUser", on_delete=models.CASCADE,related_name='extension')
    def __str__(self):
        return '<UserExtension:(id:%s,school:%s)>' % (self.id,self.school)
