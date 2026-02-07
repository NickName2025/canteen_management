from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from student.models import Dishes

def student(request):
    dishes = Dishes.objects.all()

    if request.POST.get("Gluten_free") is not None:
        dishes = dishes.exclude(is_glucose=True)
    if request.POST.get("Lactose_free") is not None:
        dishes = dishes.exclude(is_lactose=True)
    if request.POST.get("Sugar_free") is not None:
        dishes = dishes.exclude(is_sugar=True)
    if request.POST.get("Vegetarian") is not None:
        dishes = dishes.exclude(is_vegetarian=True)

    # exclude

    context = {
        "dishes": dishes,
    }

    return render(request, "student/student.html", context)

@login_required
def allergy_indication(request):
    if request.method == 'POST':
        print("POST")
        print(request.POST.get("Gluten_free"))
        print(request.POST.get("Lactose_free"))

    return render(request, "student/student.html")