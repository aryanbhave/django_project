from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('referers/', views.referers, name='blog-referers'),
    path('accounts/login', views.referers, name='accountlogin'),
    path('referers/becomeAReferer', views.becomeAReferer, name='becomeAReferer'),
]