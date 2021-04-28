from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=225)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post')


class Post(models.Model):
    title = models.CharField(max_length=225)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=225, default= 'S-Tech blog')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=225, default='Technology')
    snippet = models.CharField(max_length=225, default='Click link above to read more ...')
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='like_post')
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("article-details",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title + ' | ' + str(self.author)