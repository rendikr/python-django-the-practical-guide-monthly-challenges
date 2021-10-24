from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def january(request):
    return HttpResponse("This Works!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")


def march(request):
    return HttpResponse("Hello There Handsome!")


def month_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'This Works!'
    elif month == 'february':
        challenge_text = 'Walk for at least 20 minutes every day!'
    elif month == 'march':
        challenge_text = 'Hello there handsome!'
    else:
        return HttpResponse('This month is not supported!')

    return HttpResponse(challenge_text)
