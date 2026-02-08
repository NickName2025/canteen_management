from django.urls import path

from administrator import views

app_name = 'administrator'

urlpatterns = [
    path('administrator/', views.administrator, name='administrator'),
    path('changing_the_request_status/<int:id>/<int:accepted>/', views.changing_the_request_status, name='changing_the_request_status'),
    path('generate_report/', views.generate_report, name='generate_report'),
]