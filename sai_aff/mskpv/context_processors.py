from .models import Post, category, Comment, Reply, Emailsubscription
from .form import sub_email
from django.core.paginator import Paginator, EmptyPage
from django.contrib.sites.models import Site

def get_search_list(request):
    category_search = Post.objects.all()
    post_ads = Post.objects.all().order_by('-published_date').filter(status=1)
    paginator = Paginator(post_ads, 3)
    cat_menu = category.objects.all()

    form = sub_email()

    try:
        post_ads_post = paginator.page(1)
    except EmptyPage:
        post_ads_post = paginator.page(paginator.num_pages)

    context = {
        'cat_menu': cat_menu,
        'category_search': category_search, 
        'host': Site.objects.get_current().domain, 
        'post_ads_post': post_ads_post,
        'sub_form': form,
    }
 
    return context