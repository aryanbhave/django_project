from django.urls import path
from . import views
from django.views.generic import TemplateView
import users

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('referers/', views.referers, name='blog-referers'),
]