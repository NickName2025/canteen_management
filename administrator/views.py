from django.shortcuts import render


def administrator(request):
    return render(request, "administrator/administrator.html")