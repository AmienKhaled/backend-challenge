from django.contrib import admin
from coffee_pods import models


class PodsAdmin(admin.ModelAdmin):
    """This class to overwrite Coffee pods models appearance in admin panel"""
    list_display = ('name', 'pod_type', 'flavors', 'pack_size',)


admin.site.register(models.CoffeePods, PodsAdmin)
