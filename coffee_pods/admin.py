from django.contrib import admin
from coffee_pods import models


class PodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pod_type', 'flavors', 'pack_size',)


admin.site.register(models.CoffeePods, PodsAdmin)
