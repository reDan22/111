from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from .models import ComputerBuild

# Create your views here.
def  hello(request):
    return render(request, "hello.html")



def show_data(request):
    current_dir = os.getcwd()
    return HttpResponse(f"Current directory: {current_dir}")
def our_company (request):
    return render(request, "our_company.html")

def buildings(request):
    objects_array2 = ComputerBuild.objects.all()
    context = {"objects_array": objects_array2}
    return render(request, "buildings.html", context)

#Решение задачи тут
def task(request):
    if request.method == 'POST':
        try:
            user_input = request.POST.get('task_input', '').strip()
            elements = user_input.split(';')
            results = []

            for element in elements:
                element = element.strip()
                name, dohods_str = element.split(':')
                

                dohods_list = dohods_str.split(',')
                cleaned_dohods = []
                for item in dohods_list:
                    cleaned_dohods.append(int(item.strip()))
                dohods_list = cleaned_dohods


                avg_dohod = round(sum(dohods_list) / 3)
                results.append((name, avg_dohod))

            
            answer = str(results)
            
            return render(request, 'task.html', {'answer': answer})
        except:
            return render(request, "task.html", {'answer': "Введите корректные данные"})
    
        
    else:
        return render(request, "task.html")


   




