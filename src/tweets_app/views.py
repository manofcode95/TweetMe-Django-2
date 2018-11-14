from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.base import RedirectView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Tweet
from .forms import TweetForm
from .mixins import AddUserToForm, UserOwnerMixin
# Create your views here.

class TweetListView(ListView):
    template_name='tweets_app/tweet_list.html'

    def get_queryset(self, *args, **kwargs):
        qs=Tweet.objects.all()
        query=self.request.GET.get('q')
        if query:
            qs=qs.filter(Q(content__icontains=query)|Q(user__username__icontains=query))
        return qs

    def get_context_data(self):
        context=super(TweetListView, self).get_context_data()
        context['form']=TweetForm
        context['action_url']=reverse_lazy('tweets_app:tweet_create')
        return context

class TweetDetailView(DetailView):
    queryset=Tweet.objects.all()
    template_name='tweets_app/tweet_detail.html'

class TweetCreateView(LoginRequiredMixin , AddUserToForm,  CreateView):
    model=Tweet
    form_class=TweetForm
    

class TweetUpdateView(UserOwnerMixin, UpdateView):
    model=Tweet
    form_class=TweetForm


class TweetDeleteView(UserOwnerMixin, DeleteView):
    model=Tweet
    template_name='tweets_app/tweet_delete.html'
    success_url=reverse_lazy('tweets_app:tweet_list')

class RetweetView(View):
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        tweet=Tweet.objects.filter(pk=pk)
        print(pk)
        if tweet:
            Tweet.objects.retweet(self.request.user, tweet.first())
        return redirect('/')
