from django.urls import path

from student import views

app_name = 'student'

urlpatterns = [
    path('', views.student, name='student'),
    path('student/', views.student, name='student'),
]