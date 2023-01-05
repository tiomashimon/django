from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')


def work(request):
    return render(request, 'work.html')

def begin(request):
    return HttpResponse('Its beginning of my django experience!!!')
