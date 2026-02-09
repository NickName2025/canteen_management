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
    active_purchase_requests = PurchaseRequests.objects.all().filter(status=False) & PurchaseRequests.objects.all().filter(rejected=False) & PurchaseRequests.objects.all().filter(in_process_of_adding=False)
    processed_purchase_requests = PurchaseRequests.objects.all().exclude(status=False) | PurchaseRequests.objects.all().exclude(rejected=False)
    current_request = PurchaseRequests.objects.all().filter(in_process_of_adding=True).first()

    list_of_possible_products = get_list_of_possible_products()

    context = {
        "active_purchase_requests": active_purchase_requests,
        "processed_purchase_requests": processed_purchase_requests,
        "dishes_served": dishes_served,
        "dishes": dishes,
        "products": products,
        "list_of_possible_products": list_of_possible_products,
        "current_request": current_request
    }

    return render(request, "chef/chef.html", context)

def add_to_request(request):
    current_request = None

    dishes_served = DishesServed.objects.all()
    dishes = Dishes.objects.all()
    products = Products.objects.all()
    active_purchase_requests = PurchaseRequests.objects.all().filter(status=False) & PurchaseRequests.objects.all().filter(rejected=False)
    processed_purchase_requests = PurchaseRequests.objects.all().exclude(status=False) | PurchaseRequests.objects.all().exclude(rejected=False)
    
    if request.method == 'POST':
        request_item = request.POST.get("request_item").split(" - ")
        request_amount = request.POST.get("request_amount")

        if request_item and request_amount:
            current_request = PurchaseRequests.objects.all().filter(in_process_of_adding=True)

            if current_request:
                current_request = current_request.first()
                current_request.products_names += request_item[0]+"|"
                current_request.products_quantity += request_amount+"|"
                current_request.units_of_measurement += request_item[1]+"|"
                current_request.save()
            else:
                PurchaseRequests.objects.create(
                    products_names=request_item[0]+"|",
                    products_quantity=request_amount+"|",
                    units_of_measurement=request_item[1]+"|",
                    in_process_of_adding=True
                )

                current_request = PurchaseRequests.objects.all().get(in_process_of_adding=True)

    list_of_possible_products = get_list_of_possible_products()
    
    context = {
        "active_purchase_requests": active_purchase_requests,
        "processed_purchase_requests": processed_purchase_requests,
        "dishes_served": dishes_served,
        "dishes": dishes,
        "products": products,
        "list_of_possible_products": list_of_possible_products,
        "current_request": current_request
    }

    return render(request, "chef/chef.html", context)

def other_func(request):
    print("other func")
    print()

    return redirect(request.META['HTTP_REFERER'])

def create_a_request(request):
    current_request = PurchaseRequests.objects.all().filter(in_process_of_adding=True).first()

    if current_request:
        current_request.in_process_of_adding = False
        current_request.save()
    # if request.method == 'POST':
    #     request_item = request.POST.get("request_item").split(" - ")
    #     PurchaseRequests.objects.create(product_name=request_item[0], product_quantity=request.POST.get("request_amount"), units_of_measurement=request_item[1])

    # return redirect(request.META['HTTP_REFERER'])
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