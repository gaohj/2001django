"""user_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front import views
from cms import views as cms_view
urlpatterns = [
    # path('admin/', admin.site.urls,name='admin'),
    path('', cms_view.index,name='index'),
    path('login/', views.my_login,name='login'),
    path('logout/', views.my_logout,name='logout'),
    path('profile/', views.prifile,name='profile'),
    # path('one_to_one/', views.one_view,name='one_view'),
    # path('proxy/', views.proxy_view,name='proxy'),
    path('inherit/', views.inherit_view,name='inherit'),
    path('add_permission/', cms_view.add_permission,name='add_permission'),
    path('add_article/', cms_view.add_article,name='add_article'),
    path('operate_permission/', cms_view.operate_permission,name='operate_permission'),
    path('operate_group/', cms_view.operate_group,name='operate_group'),
]
