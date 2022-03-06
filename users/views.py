from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def first(request):
    return JsonResponse({
        "code": 200,
        "msg": '你好'
    })
