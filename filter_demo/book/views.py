from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    context = {
        'times':datetime(year=2020,month=7,day=15,hour=16,minute=30,second=10)
    }

    return render(request,'index.html',context=context)