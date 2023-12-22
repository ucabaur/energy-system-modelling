from rest_framework import viewsets
from core.models import EnergyPlant
from core.serializers import EnergyPlantSerializer


class EnergyPlantViewSet(viewsets.ModelViewSet):
    queryset = EnergyPlant.objects.all()
    serializer_class = EnergyPlantSerializer
