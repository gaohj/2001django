from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.core import validators
from django.dispatch import receiver
from django.db.models.signals import post_save
#
# class People(User):
#     # telephone = models.CharField(max_length=11)
#     class Meta:
#         proxy = True  #表示People是User的代理
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)

# class UserExtension(models.Model):
#     telephone = models.CharField(max_length=11)
#     birth = models.CharField(max_length=10,validators=[validators.MinLengthValidator(6,message="最少日期是6位")])
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
# @receiver(post_save,sender=User)
# def handler_save_userextension(sender,instance,created,**kwargs):
#     if created:
#         UserExtension.objects.create(user=instance)
#     else:
#         instance.extension.save()

class UserManager(BaseUserManager):
    def _create_user(self, telephone,username, email, password, **kwargs):
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('The given username must be set')
        user = self.model(telephone=telephone,username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    #创建普通用户
    def create_user(self, telephone,username, password,email=None,**kwargs):
        kwargs['is_staff'] = False
        kwargs['is_superuser']= False
        return self._create_user(telephone=telephone,username=username,password=password,email=email,**kwargs)

    def create_superuser(self,telephone,username,email,password,**kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True

        return self._create_user(telephone=telephone,username=username,password=password,email=email,**kwargs)

# class User(AbstractUser):
#     telephone = models.CharField(max_length=11, unique=True)
#     school = models.CharField(max_length=50)
#
#     objects = UserManager()
#     USERNAME_FIELD = 'telephone'
class User(AbstractBaseUser,PermissionsMixin):
    telephone = models.CharField(max_length=11,unique=True)
    email = models.CharField(max_length=50,validators=[validators.EmailValidator(message='请输入正确的邮箱')])
    username = models.CharField(max_length=30,validators=[validators.MinLengthValidator(6,message='用户名最少6位')])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone' #默认是以username 作为验证条件  现在以手机号作为验证条件
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username

    def get_black_list(self):
        return self.objects.filter(is_active=False)


