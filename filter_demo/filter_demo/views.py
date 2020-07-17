from  django.shortcuts import render
from datetime import datetime

def add_view(request):
    context = {
        'num1':[1,2,3],
        'num2':[4,5,6],
    }
    return render(request,'add.html',context=context)


def momentjs(request):
    context = {
        'timed': datetime(year=2020, month=7, day=15, hour=16, minute=30, second=10)
    }
    return render(request,'moment.html',context=context)
