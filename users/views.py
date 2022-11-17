from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import referrer
from django.contrib.auth.models import User
from .models import referrer
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm

# Create your views here.
def becomeAReferer(request):
    submitted=False
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/referers/')

    form=UserRegisterForm
    return render(request,'users/becomeAReferer.html',{'form':form})

def registerReferer(request):
    return render(request,'./users/becomeAReferer.html',{})

'''def addReferer(request):
    return render(request,'users/becomeAReferer.html',{})'''


'''def register(request):
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        print('form created')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            
            #Adding data to referrer table in RDS database
            ref = referrer()
            ref.firstName = form.cleaned_data.get("firstname")
            ref.lastName = form.cleaned_data.get("lastname")
            ref.university = form.cleaned_data.get("university")
            ref.company = form.cleaned_data.get("company")
            ref.role = form.cleaned_data.get("role")

            ref.save()

            messages.success(request, f'Your account has been created, you can proceed to login.')
            return redirect('referers')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})'''


'''@login_required
def profile(request):
    if request.method == "POST":
        #Remove user from referrer database and auth users as well.
        firstNameQuery = request.POST.get('changeFirst', None)
        lastNameQuery = request.POST.get('changeSecond', None)
        emailQuery = request.POST.get('changeEmail', None)
        usernamequery = request.POST.get('usernameTBD', None)
        companyQuery = request.POST.get('changeCompany', None)

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
                context = {
                    'userDB' : User.objects.all().filter(username=usernameReq),
                    'referrerDB' : referrer.objects.all().filter(username=usernameReq)
                }
                return render(request, 'users/profile.html', context)
            elif lastNameQuery:
                referrer.objects.all().filter(username=usernameReq).update(lastName=lastNameQuery)
                User.objects.all().filter(username=usernameReq).update(last_name=lastNameQuery)
                response = 'Your last name has been changed to ' + str(lastNameQuery)
                messages.success(request, response)
                context = {
                    'userDB' : User.objects.all().filter(username=usernameReq),
                    'referrerDB' : referrer.objects.all().filter(username=usernameReq)
                }
                return render(request, 'users/profile.html', context)
            elif emailQuery:
                if '@' in emailQuery:
                    referrer.objects.all().filter(username=usernameReq).update(email=emailQuery)
                    User.objects.all().filter(username=usernameReq).update(email=emailQuery)
                    response = 'Your email has been changed to ' + str(emailQuery)
                    messages.success(request, response)
                    context = {
                        'userDB' : User.objects.all().filter(username=usernameReq),
                        'referrerDB' : referrer.objects.all().filter(username=usernameReq)
                    }
                    return render(request, 'users/profile.html', context)
                else:
                    messages.info(request, 'Please type a valid email address.')
                    context = {
                        'userDB' : User.objects.all().filter(username=usernameReq),
                        'referrerDB' : referrer.objects.all().filter(username=usernameReq)
                    }
                    return render(request, 'users/profile.html', context)
            elif companyQuery:
                referrer.objects.all().filter(username=usernameReq).update(company=companyQuery)
                response = 'Your company has been changed to ' + str(companyQuery)
                messages.success(request, response)
                context = {
                    'userDB' : User.objects.all().filter(username=usernameReq),
                    'referrerDB' : referrer.objects.all().filter(username=usernameReq)
                }
                return render(request, 'users/profile.html', context)
            else:
                messages.info(request, 'There was a problem while managing your profile. Please retry.')
                context = {
                    'userDB' : User.objects.all().filter(username=usernameReq),
                    'referrerDB' : referrer.objects.all().filter(username=usernameReq)
                }
                return render(request, 'users/profile.html', context)
    else:  
        context = {
                    'userDB' : User.objects.all().filter(username=request.user.username),
                    'referrerDB' : referrer.objects.all().filter(username=request.user.username)
        }
        return render(request, 'users/profile.html', {'userDB' : User.objects.all().filter(username=request.user.username), 'referrerDB' : referrer.objects.all().filter(username=request.user.username)})

'''
# def changeData(request, username, fieldTBU, queryInput):
#     referrer.objects.all().filter(username=username).update(fieldTBU=queryInput)
#     User.objects.all().filter(username=username).update(fieldTBU=queryInput)
#     response = 'Your first name has been changed to ' + str(queryInput)
#     messages.success(request, response)
#     return render(request, 'users/profile.html')
