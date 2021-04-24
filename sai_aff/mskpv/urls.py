from django.urls import path
from django.contrib.auth import views
from . import views
from .views import post, article, Addpost_view


urlpatterns = [
    path('', views.index, name='index'),
    path('2', views.index_2, name='2'),
    path('post', post.as_view(), name='post' ),
    path('article/<int:pk>', article.as_view(), name='article-details' ),
    path('addpost/',Addpost_view.as_view(), name = 'addpost'),
    path('contact', views.contact_us,name='contact'),
]