from django.http import FileResponse
from django.shortcuts import render, redirect

from student.models import PurchasedMeals
from chef.models import PurchaseRequests, DishesServed

from openpyxl import Workbook


def administrator(request):
    money_received = 0

    purchased_meals = PurchasedMeals.objects.all()
    purchase_requests = PurchaseRequests.objects.all().exclude(status=True) & PurchaseRequests.objects.all().exclude(rejected=True)
    users = []

    for purchased_meal in purchased_meals:
        if purchased_meal.user.type == "student":
            users.append(purchased_meal.user.username)
        money_received += purchased_meal.paid_for

    context = {
        "money_received": money_received,
        "num_of_users": len(set(users)),
        "purchase_requests": purchase_requests
    }

    return render(request, "administrator/administrator.html", context)

def changing_the_request_status(request, id, accepted):
    purchase_requests = PurchaseRequests.objects.all().get(id=id)

    purchase_requests.status = bool(accepted)
    purchase_requests.rejected = not(bool(accepted))

    purchase_requests.save()

    return redirect(request.META['HTTP_REFERER'])

def generate_report(request):
    dishes_served = DishesServed.objects.all()

    dishes = {}

    for dish in dishes_served:
        if dish.dish_name not in dishes:
            dishes[dish.dish_name] = 1
        else:
            dishes[dish.dish_name] += 1

    workbook = Workbook()

    page = workbook.active
    page["A1"] = "выданные продукты"
    page["B1"] = "количество"

    i = 2

    for dish in dishes:
        page[f"A{i}"] = dish
        page[f"B{i}"] = dishes[dish]
        i += 1

    workbook.save("media/report.xlsx")

    file=open("media/report.xlsx","rb")
    response=FileResponse(file)
    return response

    

    return redirect(request.META['HTTP_REFERER'])