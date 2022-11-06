from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    groups = forms.CharField(label='Company', required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups', 'password1', 'password2']


