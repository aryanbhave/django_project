from django import forms
from django.forms import ModelForm
from .models import referrer

class UserRegisterForm(ModelForm):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    university = forms.CharField(required=True)
    company = forms.CharField(required=True)
    role = forms.CharField(required=True)
    linkedin=forms.CharField(required=True)


    class Meta:
        model = referrer
        fields = ('firstName', 'lastName','username','email', 'university', 'company', 'role', 'linkedin')

    
