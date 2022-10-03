"""rapsDaily views

views docstring
"""
# rapsDaily/views.py

#pylint: disable=missing-function-docstring
#pylint: disable=unused-argument

from django.http import HttpResponse

def index(request):
    return HttpResponse('RapsDaily - a Toronto Raptors fansite!')
