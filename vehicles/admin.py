from .models import Vehicle, Path, PathDetail, VehiclePath
from django.contrib import admin

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Path)
admin.site.register(PathDetail)
admin.site.register(VehiclePath)