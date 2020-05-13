from rest_framework import serializers
from vehicle_system.models import GeoData, Vehicle


class GeoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = ['latitude', 'longitude']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
