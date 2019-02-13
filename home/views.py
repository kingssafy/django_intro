from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
# Create your views here.
def index(request):
    print(request)
    print(type(request))
    pprint(request.META)
    return HttpResponse("Welcome to Djang!")

def dinner(request):
    menues = ["tuna", "pastas", "bob", "jjjige", "sushi"]
    return render(request, 'dinner.html', {'menues': menues})

def hello(request, name):
    context = {"name": name}
    return render(request, 'hello.html', context)

def cube(request, num):
    context = {"num": int(num)**3}
    return render(request, "cube.html", context)
