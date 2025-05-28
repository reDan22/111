from django.contrib import admin

from .models import ComputerBuild, PCConfiguration, Component, WhoIsDFS

admin.site.register(ComputerBuild)
admin.site.register(PCConfiguration)
admin.site.register(Component)
admin.site.register(WhoIsDFS)