from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #strona glówna; ścieżka, funkcja, nazwa
    path('about/', views.about, name='blog-about'),
]
