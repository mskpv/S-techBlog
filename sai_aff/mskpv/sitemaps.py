from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.published_date


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    protocol = 'https'
    
    def items(self):
        return ['index','post', 'contact']

    def location(self, item):
        return reverse(item)