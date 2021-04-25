from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, category
from .form import Postform ,Editform
from django.urls import reverse_lazy

# Create your views here.
def index(request):
   return render(request,'stechblog/index.html')

class post(ListView):
    model = Post
    template_name = 'post.html'
    ordering = ['-created_date']
    #ordering = ['-id']
    def get_context_data(self,*args, **kwargs):
        cat_menu = category.objects.all()
        context = super(post,self).get_context_data(*args,**kwargs)
        context['cat_menu'] = cat_menu
        return context

class article(DetailView):
    model = Post
    template_name = 'article.html'

class Addpost_view(CreateView):
    model = Post
    form_class = Postform
    template_name = 'add_blog_post.html'
    #fields = '__all__'

class Updatepost_view(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = Editform
    #fields = ['title','title_tag','body']

class Deletepost_view(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post')

class Addcategory_view(CreateView):
    model = category
    #form_class = Postform
    template_name = 'add_category.html'
    fields = '__all__'

def Category_view(request,cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'category.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})


def index_2(request):
    return render(request,'stechblog/index-2.html')

def contact_us(request):
    return render(request,'stechblog/Contact-us.html')