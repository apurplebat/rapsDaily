from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from blog import models
from django.db.models import Count


def home(request):
	latest_posts = models.Post.objects.published().order_by('-published')[:3]
	popular_topics = models.Topic.objects.count_topics().order_by('-blog_posts__count')[:10]
	context = {'latest_posts': latest_posts, 'popular_topics': popular_topics}
	return render(request, 'rapsDaily/home.html', context)