from django.http import JsonResponse
from django.shortcuts import redirect, render

from random import randint

from carts.models import Cart
from student.models import Dishes, PurchasedMeals

# Create your views here.

def cart_add(request, dish_slug, dish_price):
    dish = Dishes.objects.get(slug=dish_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, dish=dish)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.final_prices += dish_price + "|"
                print(cart.final_prices)
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, dish=dish, quantity=1, final_prices=dish_price+"|")

    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, dish_slug):
    print("cart_remove", request.POST)

def place_an_order(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        
        if carts.exists():
            for cart in carts:
                for i in range(cart.quantity):
                    key = ""
                    s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

                    for l in range(4):
                        key += s[randint(0, len(s) - 1)]

                    PurchasedMeals.objects.create(user=request.user, dish=cart.dish, key=key)
                cart.delete()

    return redirect(request.META['HTTP_REFERER'])

