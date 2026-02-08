from django.urls import path

from chef import views

app_name = 'chef'

urlpatterns = [
    path('chef/', views.chef, name='chef'),
    path('create_a_request/', views.create_a_request, name='create_a_request'),
]