from django.shortcuts import render ,get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy
from .form import SignUpForm, EditProfileForm, Passwordchangingform, LoginAuthForm, Profile_page_form
from django.contrib.auth.views import PasswordChangeView
from mskpv.models import Profile

# Create your views here.
class CreateProfilepageView(CreateView):
    model = Profile
    form_class = Profile_page_form
    template_name = 'registration/Create_Profile_page.html'
    #fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = Profile_page_form
    template_name = 'registration/edit_profile_page.html'
    #fields = ['bio','profile_pic','youtube_url','facebook_url','twitter_url','instagram_url']
    success_url = reverse_lazy('post')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/User_profile.html'
    
    def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

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