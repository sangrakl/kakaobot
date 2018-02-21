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

@csrf_exempt
def message(request):

    return JsonResponse(
        {
            'message': {
                'text': '내가원하는 메세지'
            }
            'keyboard': {
                'type': 'buttons',
                'buttons': ['메시지벝믄1', '메시지벝믄2', '메시지벝믄3',]
            }

        }
    )
