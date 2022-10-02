# rapsDaily/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('RapsDaily - a Toronto Raptors fansite!')