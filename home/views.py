from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime
# Create your views here.
def index(request):
    print(request)
    print(type(request))
    pprint(request.META)
    return render(request, 'index.html')

def dinner(request):
    menues = ["tuna", "pastas", "bob", "jjjige", "sushi"]
    return render(request, 'dinner.html', {'menues': menues})

def hello(request, name):
    context = {"name": name}
    return render(request, 'hello.html', context)

def cube(request, num):
    context = {"num": int(num)**3}
    return render(request, "cube.html", context)

def ping(request):
    return render(request, "ping.html")

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, "pong.html", {"data": data})

def user_new(request):
    
    return render(request, "user_new.html")

def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname': nickname, 'pwd': pwd})

def template_example(request):
    my_list = ['jjajang', 'tansu', 'jjambbong', 'yangjang']
    my_sentence = 'Life is short, you need python'
    messages = ["apple", "banana", "cucumber", "mango"]
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'template_example.html',
            {'my_list': my_list,
             'my_sentence': my_sentence,
             'messages': messages, 'empty_list': empty_list,
             'datetimenow': datetimenow,
             }
            )

def static_example(request):
    return render(request, 'static_example.html')
