from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap, StaticViewSitemap
from django.urls import path
from django.contrib.auth import views
from . import views
from .views import post, article, Addpost_view, Updatepost_view, Deletepost_view, Addcategory_view, subscription, userpost_view, SearchResultsList #, AddComment_view

sitemaps = {
    'posts': BlogPostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    #path('', views.index, name='index'),
    #path('2/', views.index_2, name='2'),
    path('', post.as_view(), name='index' ),
    path('post/', post.as_view(), name='post' ),
    path('article/<slug:slug>/', article.as_view(), name='article-details' ),
    path('addpost/',Addpost_view.as_view(), name = 'addpost'),
    path('article/edit/<slug:slug>/', Updatepost_view.as_view(), name='Update_post' ),
    path('addcategory/', Addcategory_view.as_view(), name='add_category' ),
    path('category/<str:cats>/', views.Category_view, name='category' ),
    path('article/<slug:slug>/delete/', Deletepost_view.as_view(), name='Delete_post' ),
    #path('article/<int:pk>/commend/', AddComment_view.as_view(), name='Add_comment' ),
    path('like/<slug:slug>/', views.Likeview, name='like_post' ),
    path('contact/', views.contact_us,name='contact'),
    path('Terms&Conditions/', views.Terms_Conditions,name='terms_and_conditions'),
    path('Privacy-Policy/', views.Privacy_Policy,name='Privacy_Policy'),
    path('subscription/', views.subscription,name='subscription'),
    path('mypost/<int:state>/', views.userpost_view, name='mypost' ),
    path('amazon-post/', views.amazon_post, name='amazon_post' ),
    path('amazon-mobiles/', views.amazon_mobiles, name='amazon_mobiles' ),
    path('amazon-gift/', views.amazon_gift, name='amazon_gift' ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path("search/", SearchResultsList.as_view(), name="search_results"),
]