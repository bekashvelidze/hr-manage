from django.contrib import admin
from .models import Department, Ticket, Priority, Category, Status

admin.site.register(Department)
admin.site.register(Ticket)
admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(Status)