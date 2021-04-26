from django import forms
from .models import Post, category

#choices = [('Technology','Technology'),('Entetainment','Entetainment'),('sports','sports'),('Healths','Healths')]
choices = category.objects.all().values_list('name','name')

category_list = []

for list in choices:
    category_list.append(list)

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            'author': forms.TextInput(attrs={'class': "form-control", 'value': '', 'id':'author_name', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'category': forms.Select(choices=category_list ,attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
        }

class Editform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
        }