from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

"""
posts = [
    {
        'author': 'Marcin',
        'title': 'Post 1',
        'content': 'My first post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Bartek',
        'title': 'Post 2',
        'content': 'His first post',
        'date_posted': 'September 7, 2018'
    }
]
"""

def home(request):
    context = {
        #'posts': posts#key: list
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #context - to co ma byc wyswietlone

class PostListView(ListView):
    model = Post
    #template
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']#na górze będą najnowsze, a na dole najstarsze posty

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    #return HttpResponse('<h1>About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
