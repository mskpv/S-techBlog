from django.urls import path
from .views import UserRegisterview

urlpatterns = [

path('register/', UserRegisterview.as_view(), name = 'register'),


]