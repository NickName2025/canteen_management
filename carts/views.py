from django.http import JsonResponse
from django.shortcuts import redirect, render

from random import randint

from carts.models import Cart
from student.models import Dishes, PurchasedMeals

# Create your views here.

def cart_add(request, dish_slug, dish_price, dish_quantity):
    dish = Dishes.objects.get(slug=dish_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, dish=dish)

        if dish_quantity <= dish.quantity:
            dish.quantity -= dish_quantity
            dish.save()

            if carts.exists():
                cart = carts.first()
                if cart:
                    print(dish_price)
                    cart.final_prices += str(float(dish_price)*dish_quantity) + "|"
                    print(cart.final_prices)
                    cart.quantity += dish_quantity
                    cart.save()
            else:
                Cart.objects.create(user=request.user, dish=dish, quantity=dish_quantity, final_prices=str(float(dish_price)*dish_quantity)+"|")

    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, dish_slug):
    print("cart_remove", request.POST)

def place_an_order(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)

        total_i = 0
        
        if carts.exists():
            for cart in carts:
                for i in range(cart.quantity):
                    key = ""
                    s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

                    for l in range(4):
                        key += s[randint(0, len(s) - 1)]

                    paid_for = round(float(cart.final_prices.split("|")[:-1][total_i]), 2) // cart.quantity

                    PurchasedMeals.objects.create(user=request.user, dish=cart.dish, key=key, paid_for=paid_for)
                total_i += 1
                cart.delete()

    return redirect(request.META['HTTP_REFERER'])

