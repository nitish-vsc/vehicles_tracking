from rest_framework import serializers
from .models import Vehicle, Path, PathDetail, VehiclePath,TravellLog

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_model', 'vehicle_type', 'rc_number', 'user']

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ['id', 'name', 'description', 'distance', 'user']

class VehiclesPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePath
        fields = ['id', 'vehicle', 'path', 'user']

class PathDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathDetail
        fields = ['id', 'name', 'description', 'lattitude', 'longitude', 'distance', 'arrival_time', 'depature_time', 'path']

class TravellLogSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TravellLog
        fields = ['vehicle', 'lattitude', 'longitude']