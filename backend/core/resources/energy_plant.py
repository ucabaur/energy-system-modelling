from import_export import resources
from core.models import EnergyPlant


class EnergyPlantResource(resources.ModelResource):
    class Meta:
        model = EnergyPlant
