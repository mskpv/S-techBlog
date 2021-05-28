from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, category, Comment, Reply, Sendmail, Emailsubscription
from .form import Postform ,Editform, Commentform, Replyform, sub_email
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
import os

# Create your views here.
def index(request):
   return render(request,'stechblog/index.html')

class post(ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'post.html'
    paginate_by = 9
    cats = category.objects.all()
    ordering = ['-created_date']
    #ordering = ['-id']
    def get_context_data(self,*args, **kwargs):
        cat_menu = category.objects.all()
        context = super(post,self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class article(DetailView):
    model = Post
    template_name = 'article.html' 
    form = Commentform
    formr = Replyform

    def post(self,request,*args, **kwargs):
        form = Commentform(request.POST)
        formr = Replyform(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return HttpResponseRedirect(reverse('article-details',args=[str(post.pk)]))
        if formr.is_valid():
            post = self.get_object()
            formr.instance.comment_id = request.POST['comment']
            formr.instance.post = post
            formr.save()
            print(request.POST)
            return HttpResponseRedirect(reverse('article-details',args=[str(post.pk)]))


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        data['form'] = self.form
        data['formr'] = self.formr
        return data

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
    cats_list = category.objects.all()
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    page = request.GET.get('page', 1)
    paginator = Paginator(category_posts, 9)
    try:
        category_posts = paginator.page(page)
    except PageNotAnInteger:
        category_posts = paginator.page(1)
    except EmptyPage:
        category_posts = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts , 'cat_menu': cats_list})

def Likeview(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-details',args=[str(pk)]))

def index_2(request):
    return render(request,'stechblog/index-2.html')

def amazon_post(request):
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'gaming laptop.csv')
    data = pd.read_csv(file_path)
    data = data.values
    title = 'Top Gaming Laptop to Buy in 2021'
    return render(request,'amazon_ads.html',{'data':data, 'title': title})

def amazon_mobiles(request):
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'mobiles below 10000.csv')
    data = pd.read_csv(file_path)
    data = data.values
    title = 'Mobile phones under 10,000'
    return render(request,'amazon_ads.html',{'data':data, 'title': title})

def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['body']
        Sendmail(name=name, subject=subject, email=email, body=body).save()
    return render(request,'stechblog/Contact-us.html')

def subscription(request):

    form = sub_email()
    if request.method == "POST":
        if form.is_valid():
            id = request.POST['email_sub']
            Emailsubscription(email_sub=id).save()
    return render(request, 'subscription.html')

def userpost_view(request,state):
    status_posts = Post.objects.filter(status=state).order_by('-created_date')
    page = request.GET.get('page', 1)
    #page = request.GET.get('page')
    paginator = Paginator(status_posts, 10)
    try:
        status_posts = paginator.page(page)
    except PageNotAnInteger:
        status_posts = paginator.page(1)
    except EmptyPage:
        status_posts = paginator.page(paginator.num_pages)
    return render(request, 'user_post.html',{ 'page':page,'category_posts':status_posts})