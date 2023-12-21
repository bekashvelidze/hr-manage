from django.contrib import admin
from .models import Warehouse, Item, Location, Type

# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Type)