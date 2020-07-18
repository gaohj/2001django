"""
    A viewset that provides default `create()`, post `retrieve()`, 查看某一个 `update()`, put
    `partial_update()`,patch `destroy()` delete and `list()` get 查看所有 actions.
"""
from . import views
from django.conf.urls import url

from rest_framework import routers


routers = routers.DefaultRouter()

routers.register(r'books',views.BookViewset)

#http://127.0.0.1:8000/movies/1/
urlpatterns = [
    url(r'^games/',views.GameViewset.as_view()),
    url(r'^movies/$',views.MovieViewset.as_view(
        actions={
            'get':'list',
            'post':'create',

        }
    )),
    url(r'^movies/(?P<pk>\d+)/$',views.MovieViewset.as_view(
        actions={
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }
    )),
    url(r'^users/',views.UserView.as_view()),
]
