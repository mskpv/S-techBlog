from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from mskpv.models import Profile

class Profile_page_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'image', 'youtube_url', 'facebook_url', 'twitter_url', 'instagram_url')

        widgets = {
            'image': forms.FileInput(attrs={'required': False,'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': "form-control"}),
            #'profile_pic': forms.TextInput(attrs={'class': "form-control"}),
            'youtube_url': forms.TextInput(attrs={'class': "form-control"}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'facebook_url': forms.TextInput(attrs={'class': "form-control"}),
            'twitter_url': forms.TextInput(attrs={'class': "form-control"}),
            'instagram_url': forms.TextInput(attrs={'class': "form-control"}),
        }

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1', 'password2')
    
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','last_login','date_joined')

class Passwordchangingform(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1','new_password2')

class LoginAuthForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control",'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class passwdemailform(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('email')

class Passwdresetform(SetPasswordForm):
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('new_password1','new_password2')
