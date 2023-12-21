from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    inventory = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    item_number = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    owner = models.CharField(max_length=250)
    company = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    photo_url = models.ImageField(upload_to='images')
    location = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.item_number} - {self.owner}"


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Type(models.Model):
    type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.type_name
