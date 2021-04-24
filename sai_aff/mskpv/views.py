from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .form import Postform

# Create your views here.
def index(request):
   return render(request,'stechblog/index.html')

class post(ListView):
    model = Post
    template_name = 'post.html'

class article(DetailView):
    model = Post
    template_name = 'article.html'

class Addpost_view(CreateView):
    model = Post
    form_class = Postform
    template_name = 'add_blog_post.html'
    #fields = '__all__'

def index_2(request):
    return render(request,'stechblog/index-2.html')

def contact_us(request):
    return render(request,'stechblog/Contact-us.html')