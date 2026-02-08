from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:dish_slug>/<str:dish_price>/', views.cart_add, name='cart_add'),
    path('cart_remove/<slug:dish_slug>/<str:dish_price>/', views.cart_remove, name='cart_remove'),
    path('place_an_order/', views.place_an_order, name='place_an_order'),
]