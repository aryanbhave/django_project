from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import referrer
from django.contrib.auth import get_user_model
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
        return render(request,'login1.html') 


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})