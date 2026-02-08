from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def chef(request):
    print("chef")

    return render(request, "chef/chef.html")