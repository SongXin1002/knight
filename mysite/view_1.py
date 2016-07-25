#vim: set fileencoding=utf-8:

#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response

def user_info(request):
    name = 'zbw'
    age = 24
    sex = 'man'
    #t = get_template('user_info.html')
    #html = t.render(Context(locals()))
    #return HttpResponse(html)
    return render_to_response('user_info.html',locals())



