from django.shortcuts import render

from student.models import Dishes

def student(request):
    dishes = Dishes.objects.all()

    context = {
        "dishes": dishes,
    }

    return render(request, "student/student.html", context)