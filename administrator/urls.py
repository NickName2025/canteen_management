from django.urls import path

from administrator import views

app_name = 'administrator'

urlpatterns = [
    path('administrator/', views.administrator, name='administrator'),
]