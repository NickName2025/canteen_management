from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from chef.models import DishesServed, Products, PurchaseRequests
from student.models import Dishes


def get_list_of_possible_products():
    return [("мука пшеничная", "кг"), ("вода", "л"), ("сахар", "кг"), ("растительное масло", "л"), ("сливочное масло", "г")]

def chef(request):
    dishes_served = DishesServed.objects.all()
    dishes = Dishes.objects.all()
    products = Products.objects.all()

    list_of_possible_products = products.first().get_list_of_possible_products()


    context = {
        "dishes_served": dishes_served,
        "dishes": dishes,
        "products": products,
        "list_of_possible_products": list_of_possible_products
    }

    return render(request, "chef/chef.html", context)

def create_a_request(request):
    print(Products.objects.all().first().get_list_of_possible_products())

    if request.method == 'POST':
        request_item = request.POST.get("request_item").split(" - ")
        PurchaseRequests.objects.create(product_name=request_item[0], product_quantity=request.POST.get("request_amount"), units_of_measurement=request_item[1])

    return redirect(request.META['HTTP_REFERER'])
    # dish = Dishes.objects.get(slug=dish_slug)
    
    # if request.user.is_authenticated:
    #     carts = Cart.objects.filter(user=request.user, dish=dish)

    #     if carts.exists():
    #         cart = carts.first()
    #         if cart:
    #             cart.final_prices += dish_price + "|"
    #             print(cart.final_prices)
    #             cart.quantity += 1
    #             cart.save()
    #     else:
    #         Cart.objects.create(user=request.user, dish=dish, quantity=1, final_prices=dish_price+"|")

    return redirect(request.META['HTTP_REFERER'])