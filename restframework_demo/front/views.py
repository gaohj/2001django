from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import BookSerializer,GameSerializer,MovieSerializer,UserSerializer
from .models import Book,Game,Movie,User
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from rest_framework.exceptions import APIException,NotFound
import uuid
from front.authentications import UserAuthentication
from front.permissions import UserPermission
from django.core.cache import cache
from rest_framework.response import Response
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#限制请求方法 继承于ListCreateAPIView等
# class GameViewset(ListCreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

class GameViewset(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


#身份验证是否正确
#你是否有权限
class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = UserAuthentication,
    permission_classes = UserPermission,

class UserView(CreateAPIView): #只允许post请求
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        action = request.GET.get('action')
        print(action)
        if action == 'register':
            return self.create(request,*args,**kwargs)
        elif action == 'login':
            return self.do_login(request,*args,**kwargs)
        else:
            raise APIException(detail='你想干嘛呢')
    def do_login(self,request,*args,**kwargs):
        u_name = request.data.get('u_name')
        u_password = request.data.get('u_password')

        try:
            user = User.objects.get(u_name=u_name)
        except User.DoesNotExist as e:
            raise NotFound(detail='该用户不存在')

        if u_password != user.u_password:
            raise APIException(detail='密码错误')

        #用户名 密码验证成功以后 我们生成token

        token = uuid.uuid4().hex
        cache.set(token,user.id,timeout=60*60*24*7)


        data = {
            "status":status.HTTP_200_OK,
            "message":'登录成功',
            "token":token,
        }

        return Response(data)


