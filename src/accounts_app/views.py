from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from tweets_app.models import Tweet
from .models import UserProfile
# Create your views here.
User= get_user_model()

class UserDetailView(DetailView):
    queryset=User.objects.all()
    template_name='profiles_app/user_detail.html'

    def get_object(self, **kwargs):
        username=self.kwargs.get('username')
        obj=get_object_or_404(User, username__iexact=username)
        return obj

    def get_context_data(self, *args, **kwargs):
        context=super(UserDetailView, self).get_context_data(*args, **kwargs)  
        context['is_following']=UserProfile.objects.is_following(self.request.user, self.get_object())
        return context
class ToggleFollowView(LoginRequiredMixin, View):
    def get(self, request, username, *args, **kwargs):
        to_toggle_user = get_object_or_404(User, username=username)
        if to_toggle_user:
            UserProfile.objects.toggle_follow(request_user=request.user, to_toggle_user=to_toggle_user)   
            return redirect('profiles_app:user_detail', username=username)
        return redirect('/')