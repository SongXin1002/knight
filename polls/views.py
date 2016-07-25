from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def index(request):
    HTML="<head>test</head><body><p1>this is test!</p1></body>"
    TIME = time.time()
    return HttpResponse("%s" % HTML)
