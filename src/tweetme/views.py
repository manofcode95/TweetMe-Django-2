from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.views.generic import FormView, ListView

from django.urls import reverse_lazy
from .forms import UserForm

User=get_user_model()


class RegisterView(FormView):
    template_name='registration/register.html'
    form_class=UserForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        username= form.cleaned_data.get('username')
        email= form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return super(RegisterView, self).form_valid(form)


class TweetSearchView(ListView):
    template_name='search.html'

    def get_queryset(self, *args, **kwargs):
        query=self.request.GET.get('q')
        qs=None
        if query:
            qs=User.objects.filter(username__icontains=query)
        return qs