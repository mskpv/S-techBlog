from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy
from .form import SignUpForm, EditProfileForm, Passwordchangingform,LoginAuthForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

class UserRegisterview(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditview(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('post')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = Passwordchangingform
    template_name='registration/change_password.html'
    success_url = reverse_lazy('post')


#class LoginAuthview(generic.FormView):
#    form_class = LoginAuthForm
#    template_name='registration/login.html'
#    success_url = reverse_lazy('post')