from django.urls import path
from .views import UserRegisterview , UserEditview, PasswordChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilepageView, Passwdresetview, password_reset_request, user_visit
from django.contrib.auth import views as auth_views

urlpatterns = [

path('register/', UserRegisterview.as_view(), name = 'register'),
path('edit_profile/', UserEditview.as_view(), name = 'edit_profile'),
#path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name = '')
path('password/',PasswordChangeView.as_view(), name = 'password'),
path('<int:pk>/profile/',ShowProfilePageView.as_view(), name = 'show_profile'),
path('<int:pk>/profile_edit_page/',EditProfilePageView.as_view(), name = 'show_edit_profile'),
path('create_profile_page/',CreateProfilepageView.as_view(), name = 'create_profile_page'),
path('reset_password/', password_reset_request, name ='reset_password'),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/passwd_reset_sent.html"), name ='password_reset_done'),
path('reset/<uidb64>/<token>', Passwdresetview.as_view(), name ='password_reset_confirm'),
path('reset_password_success/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/passwd_reset_success.html"), name ='password_reset_complete'),
path('user-visit/',user_visit, name='User_visit'),
]