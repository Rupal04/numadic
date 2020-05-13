from django.db import models


class Vehicle(models.Model):
    class Meta(object):
        db_table = 'vehicle'

    vehicle_license = models.CharField(primary_key=True, max_length=800, null=False, blank=False)
    model = models.CharField(max_length=800, null=False, blank=False)
    engine_number = models.CharField(max_length=800, null=False, blank=False)
    chassis_number = models.CharField(max_length=800, null=False, blank=False)


class GeoData(models.Model):
    class Meta(object):
        db_table = 'geo_data'

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    time = models.DateTimeField(null=False)
    vehicle_license = models.ForeignKey(Vehicle, blank=False, null=False, on_delete=models.CASCADE, related_name='vehicle_license_id')
