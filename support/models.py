from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    department = models.CharField(max_length=400)
    priority = models.CharField(max_length=100)
    category = models.CharField(max_length=250)
    user = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.department} - {self.user} - {self.priority} - {self.category} - {self.status}"


class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name="Statuses")

    def __str__(self):
        return self.name
