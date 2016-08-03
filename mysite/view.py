from django.http import HttpResponse
from MySQL.models import testuser

def index(request):
    test = testuser.objects.get_or_create(name = 'songxin')[0]
    return HttpResponse(test)
