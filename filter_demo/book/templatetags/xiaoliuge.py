
from datetime import datetime
from django import template

register = template.Library()
#value就是从数据库中取出来的值

@register.filter('huihui')
def my_time(value):
# 1分钟以内 显示刚刚
# 小时以内 xx分钟以前
# 以天以内 xx小时前
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    timetemp = (now-value).total_seconds()
    if timetemp < 60:
        return '%s秒以前' % int(timetemp)
    elif timetemp >= 60 and timetemp< 60*60:
        minutes = int(timetemp/60)
        return '%s分钟以前' % minutes
    elif timetemp >= 60*60 and timetemp< 60*60*24:
        hours = int(timetemp/60/60)
        return '%s小时以前' % hours
    elif timetemp >= 60*60*24 and timetemp< 60*60*24*30:
        days = int(timetemp/60/60/24)
        return '%s天以前' % days
    else:
        return value.strftime("%Y/%m/%d %H:%M:%S")

