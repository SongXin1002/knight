from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def WebLog(request):
    logfile = open("/opt/Tomcat_Background_b2b2b/logs/catalina.out")
    return HttpResponse(follow(logfile))
        
