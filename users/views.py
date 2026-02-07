from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth

from users.forms import UserRegistrationForm


def login(request):
    return render(request, 'users/login.html')

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

def logout(request):
    ...