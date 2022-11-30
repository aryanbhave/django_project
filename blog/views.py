from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import referrer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages
import tkinter
from tkinter import messagebox

User = get_user_model()

# Create your views here.
def home(request):
    if request.GET.get('query', None):
        query = request.GET.get('query', None)
        context = {
            'title': "Home",
            'query_results' : referrer.objects.all().filter(company=query).order_by('firstName') | referrer.objects.all().filter(firstName=query).order_by('lastName') | referrer.objects.all().filter(lastName=query).order_by('firstName')
        }
        return render(request, 'blog/home1.html', context)
    else:
        context = {
            'query_results' : referrer.objects.all().order_by('company')
        }
        return render(request, 'blog/home1.html', context)

def referers(request):
    context={
        'list':referrer.objects.all()
    }
    if request.user.is_authenticated:
        return render(request,'blog/referers.html',context)
    else:
        pass


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def mailuser(request, mail):
    root = tkinter.Tk()
    root.withdraw()
    useremail = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    send_mail(
        'ReferUp: You have a new referral request!',
        'Hola Amigo,\n\n' + first_name + ' ' + last_name + ' has requested for a referral at your workplace through the ReferUp portal.\n\nFirst Name: ' + first_name + '\nLast Name: ' + last_name + '\nEmail Address: ' + useremail + '\n\n\nRegards,\nTeam ReferUp',
        'cboggaram@scu.edu',
        [mail],
    )
    messagebox.showinfo("Alert", "Your request for referral has been sent to the referrer " + mail)
    return referers(request)
