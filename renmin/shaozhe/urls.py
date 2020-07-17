from django.urls import path,re_path
from . import views

app_name = 'shaozhe' #应用命令空间
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('detail/<int:shaozhe_id>/',views.detail,name='detail'),
]