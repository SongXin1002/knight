from django.http import HttpResponse
from MySQL.models import songxin

def index(request):
    test = songxin.objects.all()
    test_str = test(sex = "man")
    return HttpResponse(test_str)
