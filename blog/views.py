from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import referrer

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
        'list':[0,1,2,3,4,5,6,7,8]
    }
    if request.user.is_authenticated:
        return render(request,'blog/referers.html',context)
    else:
        return render(request,'login1.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})