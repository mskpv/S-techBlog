from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['index','post', 'contact','amazon_post','amazon_mobiles','amazon_gift']

    def location(self, item):
        return reverse(item)