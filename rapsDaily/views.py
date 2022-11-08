"""rapsDaily views

views docstring
"""
# rapsDaily/views.py

#pylint: disable=missing-function-docstring
#pylint: disable=unused-argument

from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    return HttpResponse('RapsDaily - a Toronto Raptors fansite!')
