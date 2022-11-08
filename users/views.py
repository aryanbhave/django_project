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
        firstNameQuery = request.POST.get('changeFirst', None)
        lastNameQuery = request.POST.get('changeSecond', None)
        emailQuery = request.POST.get('changeEmail', None)
        usernamequery = request.POST.get('usernameTBD', None)

        if request.user.is_authenticated:
            usernameReq = request.user.username #Originally called username
            if usernameReq == usernamequery:
                referrer.objects.all().filter(username=usernameReq).delete()
                User.objects.all().filter(username=usernameReq).delete()
                messages.success(request, f'Your account has been successfully deleted. We are sorry to see you go!')
                return redirect('logout')
            elif firstNameQuery:
                referrer.objects.all().filter(username=usernameReq).update(firstName=firstNameQuery)
                User.objects.all().filter(username=usernameReq).update(first_name=firstNameQuery)
                response = 'Your first name has been changed to ' + str(firstNameQuery)
                messages.success(request, response)
                return render(request, 'users/profile.html')
            elif lastNameQuery:
                referrer.objects.all().filter(username=usernameReq).update(lastName=lastNameQuery)
                User.objects.all().filter(username=usernameReq).update(last_name=lastNameQuery)
                response = 'Your last name has been changed to ' + str(lastNameQuery)
                messages.success(request, response)
                return render(request, 'users/profile.html')
            elif emailQuery:
                if '@' in emailQuery:
                    referrer.objects.all().filter(username=usernameReq).update(email=emailQuery)
                    User.objects.all().filter(username=usernameReq).update(email=emailQuery)
                    response = 'Your email has been changed to ' + str(emailQuery)
                    messages.success(request, response)
                    return render(request, 'users/profile.html')
                else:
                    messages.info(request, 'Please type a valid email address.')
                    return render(request, 'users/profile.html')
            else:
                messages.info(request, 'There was a problem while managing your profile. Please retry.')
                return render(request, 'users/profile.html')
    else:  
        return render(request, 'users/profile.html')


# def changeData(request, username, fieldTBU, queryInput):
#     referrer.objects.all().filter(username=username).update(fieldTBU=queryInput)
#     User.objects.all().filter(username=username).update(fieldTBU=queryInput)
#     response = 'Your first name has been changed to ' + str(queryInput)
#     messages.success(request, response)
#     return render(request, 'users/profile.html')