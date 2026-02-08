from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from student.models import Dishes, Reviews, PurchasedMeals
from chef.models import DishesServed
from carts.models import Cart

def student(request):
    print("student")
    dishes = Dishes.objects.all()
    carts = Cart.objects.all()
    purchased_meals = PurchasedMeals.objects.all().filter(user=request.user)
    not_issued_purchased_meals = purchased_meals.exclude(key="-")

    if request.POST.get("Gluten_free") is not None:
        dishes = dishes.exclude(is_glucose=True)
    if request.POST.get("Lactose_free") is not None:
        dishes = dishes.exclude(is_lactose=True)
    if request.POST.get("Sugar_free") is not None:
        dishes = dishes.exclude(is_sugar=True)
    if request.POST.get("Vegetarian") is not None:
        dishes = dishes.filter(is_vegetarian=True)

    # exclude

    context = {
        "dishes": dishes,
        "carts": carts,
        "purchased_meals": purchased_meals,
        "not_issued_purchased_meals": not_issued_purchased_meals
    }

    return render(request, "student/student.html", context)

@login_required
def allergy_indication(request):
    if request.method == 'POST':
        print(request.POST.get("Gluten_free"))
        print(request.POST.get("Lactose_free"))

    return render(request, "student/student.html")

@login_required
def sending_reviews(request):
    if request.method == 'POST':
        dish_name = request.POST.get("dish_name")
        estimation = request.POST.get("rating")
        comment = request.POST.get("comment")
        
        Reviews.objects.create(user=request.user, dish_name=dish_name, estimation=estimation, comment=comment)
        print("Отзыв успешно отправлен!")

    return redirect(request.META['HTTP_REFERER'])

@login_required
def getting_meals(request):
    if request.method == 'POST':
        code = request.POST.get("receipt_code")

        obj = PurchasedMeals.objects.all().filter(key=code)
        dishes_served = DishesServed.objects.all()

        if obj:
            print(obj)
            dishes_served.create(user=request.user, dish_name=obj.first().dish.name)
            obj.first().key = "-"
            obj.first().save()
        else:
            print("Not found")

    return redirect(request.META['HTTP_REFERER'])