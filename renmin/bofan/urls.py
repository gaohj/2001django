from django.urls import path,re_path
from . import views
app_name = 'bofan' #应用命名空间
urlpatterns = [
    # path('',views.index,name='index'),
    re_path(r'^$',views.index,name='index'),
    path('dsfadsfafadsfasdfadsfadsfasdfadsfsadfadsf/',views.login,name='login'),
    #/detail/666/
    # path('detail/'  http://127.0.0.1:9000/detail/?name=kangbazi
    path('detail/<haha_id>/',views.detail,name='detail'),
    re_path(r'^list/(?P<year>[12]\d{3})/$',views.book_list_year),
    re_path(r'^list/(?P<telephone>1[3-9]\d{9})/$',views.book_list_telephone),

]