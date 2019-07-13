from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #strona glówna; ścieżka, funkcja, nazwa
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #strona glówna; ścieżka, funkcja, nazwa; pk - primary key- odnosi się do konkretnego posta
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

#<app>/<model>_<viewtype>.html
