from django.contrib import admin
from car_app.cars.models import Car, Picture, Color, Model, Brand, Property, FuelType

# Register your models here.

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Picture)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Property)
admin.site.register(FuelType)