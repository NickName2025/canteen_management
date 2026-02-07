from django.contrib import admin

from student.models import Dishes, Reviews

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "quantity", "price", "food_intake"]
    list_editable = ["quantity"]
    search_fields = []
    list_filter = ["name", "quantity", "price", "food_intake"]

    fields = [
        "name",
        "slug",
        ("is_glucose", "is_lactose", "is_sugar", "is_vegetarian"),
        "price",
        "quantity",
        "food_intake"
    ]

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ["dish_name", "estimation"]
    list_filter = ["dish_name", "estimation"]

    fields = [
        "dish_name",
        "estimation",
        "comment",
    ]