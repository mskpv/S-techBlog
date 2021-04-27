from django.urls import path
from .views import UserRegisterview , UserEditview

urlpatterns = [

path('register/', UserRegisterview.as_view(), name = 'register'),
path('edit_profile/', UserEditview.as_view(), name = 'edit_profile'),


]