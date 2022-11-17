from django import forms
from django.forms import ModelForm
from .models import referrer

class UserRegisterForm(ModelForm):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    university = forms.CharField(required=True)
    company = forms.CharField(required=True)
    role = forms.CharField(required=True)
    linkedinURL=forms.CharField(required=True)


    class Meta:
        model = referrer
        fields = ('firstname', 'lastname','username','email', 'university', 'company', 'role', 'linkedinURL')


