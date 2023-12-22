from django.db import models
from django.contrib.postgres.fields import ArrayField


class EnergyPlant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    technology = models.CharField(max_length=100)
    set_type = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    capacity = models.FloatField(null=True, blank=True)
    efficiency = models.FloatField(null=True, blank=True)
    date_in = models.FloatField(null=True, blank=True)
    date_retrofit = models.FloatField(null=True, blank=True)
    date_out = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    volume_mm3 = models.FloatField(null=True, blank=True)
    dam_height_m = models.FloatField(null=True, blank=True)
    storage_capacity_mwh = models.FloatField(null=True, blank=True)
    eic = ArrayField(models.CharField(max_length=100), blank=True)
    project_id = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
