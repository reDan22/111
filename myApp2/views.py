from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import  MineInfo2, ProgramInfo2, CourseMateInfo2
from django.db.models import Q  # нужно для фильтрации

def about_me(request):
    return render(request, 'about_me.html')

def my_program(request):
    return render(request, 'my_program.html')

def management(request):
    return render(request, 'management.html')

def groupmates(request):
    return render(request, 'groupmates.html')






def student(request):
    search_query = request.GET.get('q', '').strip()
    coursmates = CourseMateInfo2.objects.all()

    if search_query:
        coursmates = coursmates.filter(name__contains=search_query)

    context = {
        "MineInfo2": MineInfo2.objects.first(),
        "ProgramInfo2": ProgramInfo2.objects.first(),
        "CourseMateInfo2": coursmates
    }
    return render(request, "student.html", context)






