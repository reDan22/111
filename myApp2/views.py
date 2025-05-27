from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import StudentInfo2

def about_me(request):
    return render(request, 'about_me.html')

def my_program(request):
    return render(request, 'my_program.html')

def management(request):
    return render(request, 'management.html')

def groupmates(request):
    return render(request, 'groupmates.html')
def student(request):
    objects_array2 = StudentInfo2.objects.all()
    context = {"objects_array": objects_array2}
    return render(request, "student.html", context)



