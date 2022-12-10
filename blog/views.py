from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.http import HttpResponse
from blog import forms, models
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'rapsDaily/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.published().order_by('-published')[:2]
        context.update({'latest_posts': latest_posts})

        return context

class AboutView(TemplateView):
	template_name = 'rapsDaily/about.html'


class PostListView(ListView):
	template_name = 'rapsDaily/post_list.html'
	model = models.Post
	context_object_name = 'posts'
	queryset = models.Post.objects.order_by('title')


class PostDetailView(DetailView):
    template_name = 'rapsDaily/post_detail.html'
    model = models.Post
    def get_queryset(self):
        queryset = super().get_queryset()
        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tops_list'] = models.Topic.objects.filter(blog_posts=self.get_object()).order_by('name')
        return context



class TopicListView(ListView):
	template_name = 'rapsDaily/topic_list.html'
	model = models.Topic
	context_object_name = 'topics'
	queryset = models.Topic.objects.order_by('name')


class TopicDetailView(DetailView):
	template_name = 'rapsDaily/topic_detail.html'
	model = models.Topic


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_list'] = models.Post.objects.filter(topics=self.get_object()).published().order_by('-published')
		return context



class PhotoContestView(CreateView):
    template_name = 'rapsDaily/form_photo.html'
    model = models.Contest
    #form_class = forms.PhotoContestForm
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'photo',
    ]

    def form_valid(self, form):
        # Create a "success" message
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for submitting!'
        )
        # Continue with default behaviour
        return super().form_valid(form)