from rest_framework import serializers
from core.models import EnergyPlant


class EnergyPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyPlant
        fields = "__all__"
