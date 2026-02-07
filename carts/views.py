from django.http import JsonResponse
from django.shortcuts import redirect, render

from carts.models import Cart
from student.models import Dishes

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
            Cart.objects.create(user=request.user, dish=dish, quantity=1)

    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, dish_slug):
    print("cart_remove", request.POST)