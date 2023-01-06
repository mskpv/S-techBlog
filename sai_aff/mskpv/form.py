from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Post, category, Comment, Reply, Emailsubscription

#choices = [('Technology','Technology'),('Entetainment','Entetainment'),('sports','sports'),('Healths','Healths')]
choices = category.objects.all().values_list('name','name')

category_list = []

for list in choices:
    category_list.append(list)

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            'author': forms.TextInput(attrs={'class': "form-control", 'value': '', 'id':'author_name', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'category': forms.Select(choices=category_list ,attrs={'class': "form-control"}),
            'snippet': forms.Textarea(attrs={'class': "form-control"}),
            #'body': forms.Textarea(attrs={'class': "form-control"}),
            
        }

class Editform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'category': forms.Select(choices=category_list ,attrs={'class': "form-control"}),
            'snippet': forms.Textarea(attrs={'class': "form-control"}),
            #'body': forms.Textarea(attrs={'class': "form-control"}),
        }

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'email' : forms.EmailInput(attrs={'class': "form-control"}),
        }

class Replyform(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class': "form-control", "rows":2, "cols": 10}),
        }

class sub_email(forms.ModelForm):
    class Meta:
        model = Emailsubscription
        fields = ('email_sub',)

        widgets = {
            'email_sub': forms.EmailInput(attrs={'class': "form-control",'placeholder':"Enter your email address"}),
        }
        labels = {
           'email_sub' : '',
        }
