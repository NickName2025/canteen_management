from django.shortcuts import render, redirect

from student.models import PurchasedMeals
from chef.models import PurchaseRequests


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
    print(1)