from django.contrib import admin
from .models import ScheduleLocation, ScheduleEvent

class ScheduleLocationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ScheduleEventAdmin(admin.ModelAdmin):
    list_display = ('name','location','date','time')

admin.site.register(ScheduleLocation, ScheduleLocationAdmin)
admin.site.register(ScheduleEvent, ScheduleEventAdmin)
