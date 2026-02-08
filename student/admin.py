from django.contrib import admin

from student.models import Dishes, Reviews, PurchasedMeals

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
    list_display = ["user_display", "dish_name", "estimation"]
    list_filter = ["dish_name", "estimation"]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)

@admin.register(PurchasedMeals)
class PurchasedMealsAdmin(admin.ModelAdmin):

    list_display = ["user_display", "dish_display", "key", "created_timestamp"]
    list_filter = ["created_timestamp", "user", "dish__name"]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)

    def dish_display(self, obj):
        return str(obj.dish.name)