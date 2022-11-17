from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = User.first_name
    last_name = User.last_name
    university = forms.CharField(required=True)
    company = forms.CharField(required=True)
    role = forms.CharField(required=True)
    linkedinURL=forms.CharField(required=True)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'university', 'company', 'role', 'linkedinURL']

