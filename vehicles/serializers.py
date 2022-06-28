from rest_framework import serializers
from .models import Vehicle, Path, PathDetail, VehiclePath

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_model', 'vehicle_type', 'rc_number', 'user']

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ['name', 'description', 'distcane', 'user']

class VehiclesPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePath
        fields = ['id', 'vehicle', 'path', 'user']

class PathDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathDetail
        fields = ['name', 'description', 'lattitude', 'longitude', 'distance', 'arrival_time', 'depature_time', 'path']
