from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import referrer

# Create your views here.
def home(request):
    if request.GET.get('query', None):
        query = request.GET.get('query', None)
        context = {
            'posts': Post.objects.all(),
            'query_results' : referrer.objects.all().filter(company=query)
        }
        return render(request, 'blog/home.html', context)
    else:
        context = {
            'posts': Post.objects.all(),
            'query_results' : referrer.objects.all()
        }
        return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})