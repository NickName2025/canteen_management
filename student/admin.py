from django.contrib import admin

from student.models import Dishes

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "quantity", "composition", "price", "food_intake"]
    list_editable = ["quantity"]
    search_fields = []
    list_filter = ["name", "quantity", "price", "food_intake"]
    fields = [
        "name",
        "slug",
        "composition",
        "price",
        "quantity",
        "food_intake"
    ]