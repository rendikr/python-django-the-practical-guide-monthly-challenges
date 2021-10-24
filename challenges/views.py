from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def january(request):
    return HttpResponse("This Works!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")
