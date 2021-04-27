from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .form import SignUpForm

# Create your views here.

class UserRegisterview(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditview(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('post')

    def get_object(self):
        return self.request.user


