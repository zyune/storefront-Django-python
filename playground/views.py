from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def caculate():
    x=1
    y=2
    return x+y
def say_hello(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    x=caculate()
    return render(request, 'hello.html' ,{'name':'aaaa'})