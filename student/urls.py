from django.urls import path

from student import views

app_name = 'student'

urlpatterns = [
    path('student/', views.student, name='student'),
    path('student/', views.allergy_indication, name='allergy_indication'),
    path('sending_reviews/', views.sending_reviews, name='sending_reviews'),
]