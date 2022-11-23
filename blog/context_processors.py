from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse
from blog import models
from django.db.models import Count


def base_context(request):
	popular_topics = models.Topic.objects.count_topics().order_by('-blog_posts__count')[:3]
	#popular_topics = models.Topic.objects.all()
	print(popular_topics)
	return {'popular_topics': popular_topics}