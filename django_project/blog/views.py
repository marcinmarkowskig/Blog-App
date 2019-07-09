from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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

def about(request):
    #return HttpResponse('<h1>About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
