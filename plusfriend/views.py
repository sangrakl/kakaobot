from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def keyboard(request):

    return JsonResponse(
        {
        'type' : 'buttons',
        'buttons': ['버튼1', '버튼2', '버튼3',]
        }
    )
