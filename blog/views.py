from typing import Optional
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    return render(request,"blog/home.html", context = {"posts":post.objects.all()})


class PostView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
def about(request):
    return render(request, "blog/about.html")


class PostDetailview(DetailView):
    model = post
    
class CreatePostview(LoginRequiredMixin,CreateView):
    model = post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdatePostview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False