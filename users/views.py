from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import referrer
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            
            #Adding data to referrer table in database
            ref = referrer()
            ref.username = form.cleaned_data.get("username")
            ref.firstName = form.cleaned_data.get("first_name")
            ref.lastName = form.cleaned_data.get("last_name")
            ref.email = form.cleaned_data.get("email")
            ref.company = form.cleaned_data.get("groups")
            ref.save()

            messages.success(request, f'Your account has been created, you can proceed to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        #Remove user from referrer database and auth users as well.
        query = request.POST.get('usernameTBD', None)
        print(query)

        if request.user.is_authenticated:
            username = request.user.username
            if username == query:
                referrer.objects.all().filter(username=query).delete()
                User.objects.all().filter(username=query).delete()
                messages.success(request, f'Your account has been successfully deleted. We are sorry to see you go!')
                return redirect('logout')
            else:
                messages.info(request, 'The username was incorrect.')
                return render(request, 'users/profile.html')
    else:  
        return render(request, 'users/profile.html')
