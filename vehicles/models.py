from django.db import models
from users.models import RegisterUser

# Create your models here.

class Path(models.Model):
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    distance = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    vehicle_model = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    rc_number = models.CharField(max_length=20, default='', null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_model

class VehiclePath(models.Model):
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)


class PathDetail(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    lattitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    distance = models.IntegerField()
    arrival_time =  models.DateTimeField(default=None)
    depature_time = models.DateTimeField(default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TravellLog(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    lattitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)