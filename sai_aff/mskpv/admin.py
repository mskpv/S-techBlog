from django.contrib import admin
from .models import Post, category, Profile, Comment, Reply, Sendmail, Emailsubscription

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("status",)

admin.site.register(Post,PostAdmin)
admin.site.register(category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Sendmail)
admin.site.register(Emailsubscription)