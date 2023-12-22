from django.contrib import admin

from core.models import EnergyPlant

from .energy_plant import EnergyPlantAdmin

admin.site.register(EnergyPlant, EnergyPlantAdmin)
