from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from core.resources import EnergyPlantResource


class EnergyPlantAdmin(ImportExportModelAdmin):
    resource_class = EnergyPlantResource
    list_display = (
        "id",
        "name",
        "fuel_type",
        "technology",
        "set_type",
        "country",
        "capacity",
    )
    search_fields = ["name", "country", "fuel_type"]
    list_filter = ("technology", "set_type", "country")
