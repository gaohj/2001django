from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'username':'kangbazi'
    }
    return render(request,'index.html',context=context)

def qf(request):
    return render(request, 'qianfeng.html')