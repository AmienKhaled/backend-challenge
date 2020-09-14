from django.contrib import admin
from coffee_machines import models


class MachinesAdmin(admin.ModelAdmin):
    list_display  = ('name', 'machine_type', 'machine_class', 'water_line_compatiple',)


admin.site.register(models.CoffeeMachines, MachinesAdmin)
