from asgiref.timeout import timeout
from django.shortcuts import render
from django.core.cache import cache
from django.http import  HttpResponse

# Create your views here.
def testView(request):
    x = cache.get('chabi')
    print(x)

    cache.set('chabi', 'kamra', timeout=500)
    return HttpResponse('abc')
