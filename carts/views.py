from django.shortcuts import render

# Create your views here.

def cart_add(request):
    print("cart_add", request.POST)

def cart_remove(request):
    print("cart_remove", request.POST)