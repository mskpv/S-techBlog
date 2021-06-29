from django.shortcuts import render ,get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy
from .form import SignUpForm, EditProfileForm, Passwordchangingform, LoginAuthForm, Profile_page_form, Passwdresetform, passwdemailform
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from mskpv.models import Profile, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.sites.models import Site


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
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        posts = []
        for i in Post.objects.all().order_by('-published_date').filter(status=1):
            if i.author.profile.id == self.kwargs['pk']:
                posts.append(i)
        page = self.request.GET.get('page', 1)
        paginator = Paginator(posts, 4)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        context['page_user'] = page_user
        context['posts'] = posts
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

class Passwdresetview(PasswordResetConfirmView):
    form_class = Passwdresetform
    template_name='registration/passwd_reset_form.html'

#class passwdemailview(PasswordResetView):
#    form_class = passwdemailform
#    template_name = 'registration/reset_passwd.html'

def password_reset_request(request):
 if request.method == "POST":
    password_reset_form = passwdemailform(request.POST)
    if password_reset_form.is_valid():
        data = password_reset_form.cleaned_data['email']
        associated_users = User.objects.filter(Q(email=data))
        if associated_users.exists():
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "registration/password_reset_email.txt"
                c = {
                "email":user.email,
                'domain':Site.objects.get_current().domain,
                'site_name': 'Website',
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                subject = "Your Password Reset"
                body = email
                sender_email = "support@stechmpv.xyz"
                receiver_email = user.email
                password = "$@!tech.!n.T@m!l"

                # Create a multipart message and set headers
                message = MIMEMultipart();message["From"] = sender_email;message["To"] = receiver_email;message["Subject"] = subject
                message.attach(MIMEText(body, "plain"))
                text = message.as_string()
                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("mail.stechmpv.xyz", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, text)
                except:
                    return HttpResponse('Invalid header found.')
                return redirect ("/members/reset_password_sent/")
 password_reset_form = passwdemailform()
 return render(request=request, template_name="registration/reset_passwd.html", context={"form":password_reset_form})

#class LoginAuthview(generic.FormView):
#    form_class = LoginAuthForm
#    template_name='registration/login.html'
#    success_url = reverse_lazy('post')