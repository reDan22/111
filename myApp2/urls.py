from django.urls import path
from . import views
app_name = "myApp2" 
urlpatterns = [
    path('about/', views.about_me, name='about_me'),
    path('program/', views.my_program, name='my_program'),
    path('management/', views.management, name='management'),
    path('groupmates/', views.groupmates, name='groupmates'),
    path("student/", views.student, name="student"),
]
