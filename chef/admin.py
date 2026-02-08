from django.contrib import admin

from chef.models import DishesServed, Products, PurchaseRequests

admin.site.register(DishesServed)
admin.site.register(Products)
admin.site.register(PurchaseRequests)