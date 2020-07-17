from django.shortcuts import render
def index(request):
    context = {
        'books':[
            '红楼梦',
            '水浒传',
            '三国演义',
            '西游记',
        ],
        'persons':{
            'username':'huihui',
            'country':'china',
        },
        'bookses':[
            {
                'name':'python从入门到放弃',
                'author':'程序员小白',
                'price':100
            },
            {
                'name': 'mysql从删库到跑路',
                'author': '程序员小作',
                'price': 50
            },
            {
                'name': 'java从入门到绝望',
                'author': '程序员小绝',
                'price': 65
            },
            {
                'name': 'js从看一眼到闭眼',
                'author': '程序员小毕',
                'price': 32
            },
        ],
        'comments':[
            '这首歌是这样的唱的',
        ]
    }

    return render(request,'index.html',context=context)