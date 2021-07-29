from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("<h1>This is our Home page</h1>")

def News(request):
    return HttpResponse("<h1>This is our lastest News</h1>")

def Contact(request):
    return HttpResponse("<h1>This is our contact page</h1>")