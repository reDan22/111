"""
URL configuration for project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views
app_name = "myApp1"
 
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path("show_data/", views.show_data),
    path("our_company/", views.our_company, name="our_company"),
    path("task/", views.task, name="task"),
    path("buildings/", views.buildings, name="buildings"),
    path('pc-configurator/', views.pc_configurator, name='pc_configurator'),
    path('orders/', views.orders, name='orders'),
]
