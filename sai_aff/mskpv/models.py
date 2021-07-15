from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField
from django.utils.text import slugify
import random, string
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

# Create your models here.


def validate_image(image):
    try:
        file_size = image.file.size
        limit_kb = 150
        w, h = get_image_dimensions(image.file)
        if file_size > limit_kb * 1024:
            raise ValidationError("Max size of file is {} KB and max width = 800px, max height = 400px".format(limit_kb))
        elif h > 400:
            raise ValidationError("Image should have Max width = 800px, max height = 400px")

    except  OSError:
        return


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='temp/')
    header_image = models.TextField(null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('post')

class category(models.Model):
    name = models.CharField(max_length=225)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post')

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(null=True, blank=True, upload_to='temp/',validators=[validate_image])
    header_image = models.TextField(null=True, blank=True)
    title_tag = models.CharField(max_length=225, default= 'S-Tech blog')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=225, default='---')
    snippet = models.CharField(max_length=225)
    slug = models.SlugField(max_length = 250, null = True, blank = True, unique=True)
    #body = HTMLField()
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='like_post',blank=True)
    published_date = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("article-details",kwargs={'slug': self.slug})

    def __str__(self):
        return self.title + ' | ' + str(self.author)

def base64String(sender, instance, *args, **kwargs):
    import base64
    try:
        header_image = "data:image/jpeg;base64,"+base64.b64encode(instance.image.read()).decode('utf-8')
    except ValueError:
        header_image = ''
    except OSError:
        return  
    instance.header_image = header_image

pre_save.connect(base64String, sender=Post)

pre_save.connect(base64String, sender=Profile)

def random_string_generator(size=10, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    klass = instance.__class__

    while True:
        if not klass.objects.filter(slug=slug).exists():
            return slug

        slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
            )
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
       instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = False
        self.save()

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    class Meta:
        ordering = ['-date_added']

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, related_name='replies')
    reply_body = models.TextField(max_length=500)
    #name = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment)

class Sendmail(models.Model):
    name = models.CharField(max_length=225)
    subject = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.subject)

class Emailsubscription(models.Model):
    email_sub = models.EmailField(unique=True)

    def __str__(self):
        return self.email_sub