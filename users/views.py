from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                print(f"{username}, Вы вошли в аккаунт")
                
                if user.type == "student":
                    return HttpResponseRedirect(reverse('student:student'))
                elif user.type == "chef":
                    return HttpResponseRedirect(reverse('chef:chef'))
                elif user.type == "administrator":
                    return HttpResponseRedirect(reverse('administrator:administrator'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid(): 
            form.save()

            user = form.instance
            user.type = "student"
            user.save()

            auth.login(request, user)
            print("Вы успешно зарегистрировались и вошли в аккаунт")
            
            return HttpResponseRedirect(reverse('student:student'))
    else:
        form = UserRegistrationForm()

    context = {
        "form": form
    }

    return render(request, 'users/registration.html', context)

@login_required
def logout(request):
    print(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('user:login'))