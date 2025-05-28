from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from .models import ComputerBuild, PCConfiguration, Component, WhoIsDFS
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PCConfigForm
from django.http import JsonResponse

from django.db.models import Avg, Count, Sum
from datetime import datetime
from django.views.decorators.csrf import csrf_protect

def get_component_price(request, component_id):
    try:
        component = Component.objects.get(id=component_id)
        return JsonResponse({'price': str(component.price)})
    except Component.DoesNotExist:
        return JsonResponse({'error': 'Component not found'}, status=404)

# Create your views here.
def  hello(request):
    return render(request, "hello.html")



def show_data(request):
    current_dir = os.getcwd()
    return HttpResponse(f"Current directory: {current_dir}")
def our_company (request):
    objects_array2 = WhoIsDFS.objects.all()
    context = {"objects_array": objects_array2}
    return render(request, "our_company.html", context)

def buildings(request):
    objects_array2 = ComputerBuild.objects.all()
    context = {"objects_array": objects_array2}
    return render(request, "buildings.html", context)



@csrf_protect
def orders(request):
    all_orders = PCConfiguration.objects.all()

    if request.method == 'POST':
        selected_month = request.POST.get('month')
    else:
        selected_month = None

    filtered_orders = all_orders
    formatted_selected_month = None

    if selected_month:
        try:
            month_date = datetime.strptime(selected_month, '%Y-%m')
            filtered_orders = all_orders.filter(
                created_at__year=month_date.year,
                created_at__month=month_date.month
            )
            formatted_selected_month = month_date.strftime('%B %Y').capitalize()
        except ValueError:
            pass

    total_stats = all_orders.aggregate(
        total_orders=Count('id'),
        total_revenue=Sum('total_price'),
        avg_order=Avg('total_price')
    )

    filtered_stats = filtered_orders.aggregate(
        total_orders=Count('id'),
        total_revenue=Sum('total_price'),
        avg_order=Avg('total_price')
    )

    available_months = PCConfiguration.objects.dates('created_at', 'month', order='DESC')

    context = {
        'objects_array': filtered_orders,
        'all_orders_stats': total_stats,
        'filtered_stats': filtered_stats,
        'available_months': available_months,
        'selected_month': selected_month,
        'formatted_selected_month': formatted_selected_month,
    }

    return render(request, "orders.html", context)


def pc_configurator(request):
    if request.method == 'POST':
        form = PCConfigForm(request.POST)
        if form.is_valid():
            order = form.save()

            # Сохраняем данные в сессии для дальнейшего использования (например, для конфигурации в заказе)
            request.session['cpu'] = form.cleaned_data['cpu'].id
            request.session['gpu'] = form.cleaned_data['gpu'].id
            request.session['ram'] = form.cleaned_data['ram'].id
            request.session['ssd'] = form.cleaned_data['ssd'].id

            context = {
                'form': form,
                'success_message': f'Заказ #{order.id} создан! Сумма: {order.total_price} руб.',
                'last_order': order
            }
            return render(request, 'pc_configurator.html', context)
    else:
        initial_data = {}

        # Извлекаем только если форма еще не была отправлена (через сессию или URL параметры)
        if not request.session.get('form_submitted', False):  # Проверка, что форма еще не отправлялась
            cpu_id = request.session.get('cpu')
            gpu_id = request.session.get('gpu')
            ram_id = request.session.get('ram')
            ssd_id = request.session.get('ssd')

            # Если данные в сессии есть, инициализируем их в форму
            if cpu_id:
                initial_data['cpu'] = Component.objects.get(id=cpu_id, category='CPU')
            if gpu_id:
                initial_data['gpu'] = Component.objects.get(id=gpu_id, category='GPU')
            if ram_id:
                initial_data['ram'] = Component.objects.get(id=ram_id, category='RAM')
            if ssd_id:
                initial_data['ssd'] = Component.objects.get(id=ssd_id, category='SSD')

            # Если данных в GET-запросе нет, будем искать по URL-параметрам
            try:
                if 'cpu' in request.GET:
                    initial_data['cpu'] = Component.objects.get(id=request.GET['cpu'], category='CPU')
                if 'gpu' in request.GET:
                    initial_data['gpu'] = Component.objects.get(id=request.GET['gpu'], category='GPU')
                if 'ram' in request.GET:
                    initial_data['ram'] = Component.objects.get(id=request.GET['ram'], category='RAM')
                if 'ssd' in request.GET:
                    initial_data['ssd'] = Component.objects.get(id=request.GET['ssd'], category='SSD')
            except Component.DoesNotExist:
                pass  # Если компонент не найден — игнорируем

        form = PCConfigForm(initial=initial_data)

    return render(request, 'pc_configurator.html', {'form': form})





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


   




