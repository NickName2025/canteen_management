from django.urls import path

from student import views

app_name = 'student'

urlpatterns = [
    path('student/', views.student, name='student'),
    path('allergy_indication/', views.allergy_indication, name='allergy_indication'),
    path('sending_reviews/', views.sending_reviews, name='sending_reviews'),
    path('getting_meals/', views.getting_meals, name='getting_meals'),
]