from django.db import models

class ScheduleLocation(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class ScheduleEvent(models.Model):
    name = models.CharField(max_length=400)
    location = models.ForeignKey(ScheduleLocation, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
