from django.http import HttpResponse

def cookies(request):
    response = HttpResponse(request.COOKIES)
    if "sessionid" in request.COOKIES:
        id = request.COOKIES["sessionid"]
        return HttpResponse(id)

