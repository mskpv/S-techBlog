from django.contrib import admin
from .models import Post, category, Profile, Comment, Reply, Sendmail, Emailsubscription

# Register your models here.

admin.site.register(Post)
admin.site.register(category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Sendmail)
admin.site.register(Emailsubscription)