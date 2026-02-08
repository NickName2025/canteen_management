from django.urls import path

from chef import views

app_name = 'chef'

urlpatterns = [
    path('chef/', views.chef, name='chef'),
]